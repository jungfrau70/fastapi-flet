# https://flet.dev/docs/controls/plotlychart
import flet as ft
import requests
import pandas as pd
import plotly.express as px
from flet.plotly_chart import PlotlyChart

# Function to fetch data from the backend
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

# Function to create chart
def create_chart():
    ohlc_data, ema20, ema50, ema100, ema200 = fetch_data()
    df = pd.DataFrame(ohlc_data)
    fig = px.line(df, x="timestamp", y="close")
    return fig

# Flet app
def main(page: ft.Page):
    page.title = "Stock Data Dashboard"
    
    # State to track login status
    is_logged_in = False

    def login(e):
        nonlocal is_logged_in
        username = username_field.value
        password = password_field.value

        response = requests.post("http://127.0.0.1:8000/login", json={"username": username, "password": password})
        if response.status_code == 200:
            is_logged_in = True
            result.value = "Login successful"
            show_dashboard()
        else:
            result.value = "Login failed"
        page.update()

    def signup(e):
        username = username_field.value
        password = password_field.value

        response = requests.post("http://127.0.0.1:8000/signup", json={"username": username, "password": password})
        if response.status_code == 200:
            result.value = "Signup successful"
        else:
            result.value = "Signup failed"
        page.update()

    def show_dashboard():
        page.clean()
        fig = create_chart()
        plot = PlotlyChart(fig)
        page.add(plot)

    def show_login_page(e):
        page.clean()
        page.add(
            ft.Column(
                controls=[
                    username_field,
                    password_field,
                    ft.ElevatedButton(text="Login", on_click=login),
                    ft.ElevatedButton(text="Sign Up", on_click=signup),
                    result
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    username_field = ft.TextField(label="Username")
    password_field = ft.TextField(label="Password", password=True)
    result = ft.Text()

    apple_image = ft.Image(src="./static/images/apple.png", width=100, height=100)

    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        apple_image,
                        ft.Text("Welcome to the Stock Data Dashboard"),
                        ft.ElevatedButton(text="Login", on_click=show_login_page)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
