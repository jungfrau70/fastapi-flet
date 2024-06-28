import flet as ft
import requests
import pandas as pd
import plotly.express as px
from flet.plotly_chart import PlotlyChart

class DataFetcher:
    @staticmethod
    def fetch_data():
        ohlc_response = requests.get("http://127.0.0.1:8000/ohlc")
        ema20_response = requests.get("http://127.0.0.1:8000/ema?period=20")
        ema50_response = requests.get("http://127.0.0.1:8000/ema?period=50")
        ema100_response = requests.get("http://127.0.0.1:8000/ema?period=100")
        ema200_response = requests.get("http://127.0.0.1:8000/ema?period=200")

        ohlc_data = ohlc_response.json()["data"]
        ema20 = ema20_response.json()
        ema50 = ema50_response.json()
        ema100 = ema100_response.json()
        ema200 = ema200_response.json()

        return ohlc_data, ema20, ema50, ema100, ema200

    @staticmethod
    def create_chart():
        ohlc_data, ema20, ema50, ema100, ema200 = DataFetcher.fetch_data()
        df = pd.DataFrame(ohlc_data)
        fig = px.line(df, x="timestamp", y="close")
        return fig

class Authentication:
    @staticmethod
    def login(username, password):
        response = requests.post("http://127.0.0.1:8000/login", json={"username": username, "password": password})
        return response.status_code == 200

    @staticmethod
    def signup(username, password):
        response = requests.post("http://127.0.0.1:8000/signup", json={"username": username, "password": password})
        return response.status_code == 200

class StockDashboardApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.is_logged_in = False
        self.username_field = ft.TextField(label="Username")
        self.password_field = ft.TextField(label="Password", password=True)
        self.result = ft.Text()
        self.apple_image = ft.Image(src="./static/images/apple.png", width=100, height=100)

    def login(self, e):
        username = self.username_field.value
        password = self.password_field.value
        if Authentication.login(username, password):
            self.is_logged_in = True
            self.result.value = "Login successful"
            self.show_dashboard()
        else:
            self.result.value = "Login failed"
        self.page.update()

    def signup(self, e):
        username = self.username_field.value
        password = self.password_field.value
        if Authentication.signup(username, password):
            self.result.value = "Signup successful"
        else:
            self.result.value = "Signup failed"
        self.page.update()

    def show_dashboard(self):
        self.page.clean()
        fig = DataFetcher.create_chart()
        plot = PlotlyChart(fig)
        self.page.add(plot)

    def show_login_page(self, e=None):
        self.page.clean()
        self.page.add(
            ft.Column(
                controls=[
                    self.username_field,
                    self.password_field,
                    ft.ElevatedButton(text="Login", on_click=self.login),
                    ft.ElevatedButton(text="Sign Up", on_click=self.signup),
                    self.result
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.page.update()

    def main(self):
        self.page.title = "Stock Data Dashboard"
        self.page.add(
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            self.apple_image,
                            ft.Text("Welcome to 챗지피티 앱"),
                            ft.ElevatedButton(text="Login", on_click=self.show_login_page)
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
    app = StockDashboardApp(page)
    app.main()

ft.app(target=main)
