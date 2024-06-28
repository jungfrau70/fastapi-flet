import flet as ft
import requests
from flet.plotly_chart import PlotlyChart

class WelcomePage:
    def __init__(self, page: ft.Page, app):
        self.page = page
        self.app = app
        self.init_ui()

    def init_ui(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Image(src="./static/images/apple.png", width=100, height=100),
                            ft.Text("Welcome to the Stock Data Dashboard"),
                            ft.ElevatedButton(text="Login", on_click=self.app.show_login_page)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.page.update()

class DashboardPage:
    def __init__(self, page: ft.Page, app):
        self.page = page
        self.app = app
        self.init_ui()

    def init_ui(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                controls=[
                    ft.Text("Welcome to the Dashboard"),
                    ft.ElevatedButton(text="Logout", on_click=self.app.logout),
                    ft.ElevatedButton(text="Refresh Data", on_click=self.app.refresh_data),
                    self.app.result
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.page.update()

class DashboardApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Stock Data Dashboard"
        self.is_logged_in = False
        self.result = ft.Text()

        self.username_field = ft.TextField(label="Username")
        self.password_field = ft.TextField(label="Password", password=True)

        self.welcome_page = WelcomePage(page, self)
        self.dashboard_page = DashboardPage(page, self)

    def show_login_page(self, e=None):
        self.welcome_page.init_ui()

    def login(self, e):
        username = self.username_field.value
        password = self.password_field.value

        response = requests.post("http://127.0.0.1:8000/login", json={"username": username, "password": password})
        if response.status_code == 200:
            self.is_logged_in = True
            self.result.value = "Login successful"
            self.show_dashboard_page()
        else:
            self.result.value = "Login failed"
        self.page.update()

    def show_dashboard_page(self):
        self.dashboard_page.init_ui()

    def logout(self, e):
        self.is_logged_in = False
        self.result.value = ""
        self.show_login_page()

    def refresh_data(self, e):
        # Implement data refresh logic here
        pass

def main(page: ft.Page):
    app = DashboardApp(page)
    app.show_dashboard_page()

ft.app(target=main)
