import flet as ft  # Flet 패키지를 ft로 임포트합니다.
import requests  # HTTP 요청을 보내기 위해 requests 패키지를 임포트합니다.
import pandas as pd  # 데이터 프레임 처리를 위해 pandas 패키지를 임포트합니다.
import plotly.express as px  # Plotly Express를 px로 임포트하여 데이터 시각화를 간편하게 합니다.
from flet.plotly_chart import PlotlyChart  # Flet에서 PlotlyChart 클래스를 임포트합니다.

class WelcomeApp:
    def __init__(self, page: ft.Page):
        # DashboardApp 클래스의 생성자입니다. 페이지를 초기화하고 필요한 요소들을 설정합니다.
        self.page = page
        self.page.title = "Stock Data Dashboard"
        self.is_logged_in = False

        # 사용자 이름과 비밀번호 입력 필드를 생성합니다.
        self.username_field = ft.TextField(label="Username")
        self.password_field = ft.TextField(label="Password", password=True)
        self.result = ft.Text()

        # 로고 이미지를 생성합니다.
        self.apple_image = ft.Image(src="./static/images/apple.png", width=100, height=100)
        
        # 초기 환영 페이지를 표시합니다.
        self.show_welcome_page()

    def fetch_data(self):
        # 주식 데이터를 가져오기 위해 여러 API 엔드포인트에 HTTP GET 요청을 보냅니다.
        ohlc_response = requests.get("http://127.0.0.1:8000/ohlc")
        ema20_response = requests.get("http://127.0.0.1:8000/ema?period=20")
        ema50_response = requests.get("http://127.0.0.1:8000/ema?period=50")
        ema100_response = requests.get("http://127.0.0.1:8000/ema?period=100")
        ema200_response = requests.get("http://127.0.0.1:8000/ema?period=200")

        # 각 응답에서 JSON 데이터를 추출합니다.
        ohlc_data = ohlc_response.json()["data"]
        ema20 = ema20_response.json()
        ema50 = ema50_response.json()
        ema100 = ema100_response.json()
        ema200 = ema200_response.json()

        # 데이터를 반환합니다.
        return ohlc_data, ema20, ema50, ema100, ema200

    def create_chart(self):
        # 데이터를 가져와서 차트를 생성합니다.
        ohlc_data, ema20, ema50, ema100, ema200 = self.fetch_data()
        df = pd.DataFrame(ohlc_data)  # OHLC 데이터를 데이터프레임으로 변환합니다.
        fig = px.line(df, x="timestamp", y="close")  # 종가를 시간에 따라 라인 차트로 그립니다.
        return fig

    def login(self, e):
        # 로그인 처리 함수입니다.
        username = self.username_field.value
        password = self.password_field.value

        # 로그인 API 엔드포인트에 사용자 이름과 비밀번호를 포함한 POST 요청을 보냅니다.
        response = requests.post("http://127.0.0.1:8000/login", json={"username": username, "password": password})
        if response.status_code == 200:
            self.is_logged_in = True
            self.result.value = "Login successful"  # 로그인 성공 시 메시지를 업데이트합니다.
            self.show_dashboard()  # 대시보드를 표시합니다.
        else:
            self.result.value = "Login failed"  # 로그인 실패 시 메시지를 업데이트합니다.
        self.page.update()  # 페이지를 업데이트합니다.

    def signup(self, e):
        # 회원가입 처리 함수입니다.
        username = self.username_field.value
        password = self.password_field.value

        # 회원가입 API 엔드포인트에 사용자 이름과 비밀번호를 포함한 POST 요청을 보냅니다.
        response = requests.post("http://127.0.0.1:8000/signup", json={"username": username, "password": password})
        if response.status_code == 200:
            self.result.value = "Signup successful"  # 회원가입 성공 시 메시지를 업데이트합니다.
        else:
            self.result.value = "Signup failed"  # 회원가입 실패 시 메시지를 업데이트합니다.
        self.page.update()  # 페이지를 업데이트합니다.

    def show_dashboard(self):
        # 대시보드를 표시하는 함수입니다.
        self.page.clean()  # 페이지를 초기화합니다.
        fig = self.create_chart()  # 차트를 생성합니다.
        plot = PlotlyChart(fig)  # PlotlyChart 객체를 생성합니다.
        self.page.add(plot)  # 페이지에 차트를 추가합니다.

    def show_login_page(self, e):
        # 로그인 페이지를 표시하는 함수입니다.
        self.page.clean()  # 페이지를 초기화합니다.
        self.page.add(
            ft.Column(
                controls=[
                    self.username_field,  # 사용자 이름 입력 필드를 추가합니다.
                    self.password_field,  # 비밀번호 입력 필드를 추가합니다.
                    ft.ElevatedButton(text="Login", on_click=self.login),  # 로그인 버튼을 추가합니다.
                    ft.ElevatedButton(text="Sign Up", on_click=self.signup),  # 회원가입 버튼을 추가합니다.
                    self.result  # 결과 메시지를 표시합니다.
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.page.update()  # 페이지를 업데이트합니다.

    def show_welcome_page(self):
        # 환영 페이지를 표시하는 함수입니다.
        self.page.add(
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            self.apple_image,  # 로고 이미지를 추가합니다.
                            ft.Text("Welcome to the Stock Data Dashboard"),  # 환영 메시지를 추가합니다.
                            ft.ElevatedButton(text="Login", on_click=self.show_login_page)  # 로그인 버튼을 추가합니다.
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

def main(page: ft.Page):
    # 메인 함수입니다. DashboardApp 클래스를 인스턴스화합니다.
    WelcomeApp(page)

# Flet 앱을 실행하고 main 함수를 타겟으로 설정합니다.
ft.app(target=main)
