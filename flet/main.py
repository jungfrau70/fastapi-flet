import flet as ft
import requests
import chart as plotly
from flet.plotly_chart import PlotlyChart

# WelcomePage class to display the welcome screen
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
                            ft.Text("Welcome to the Stock Data Dashboard"),
                            ft.ElevatedButton(text="Login", on_click=self.app.show_login_page),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Image(src="./static/images/apple.png", width=100, height=100)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.page.update()

# DashboardPage class to display the main dashboard after login
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
                    ft.Row(
                        controls=[
                            ft.Text("Welcome to the Dashboard"),
                            ft.ElevatedButton(text="Logout", on_click=self.app.logout),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.ElevatedButton(text="Plot Data", on_click=self.app.show_plot_data_page),
                    self.app.result
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.page.update()

# # SignupPage class to display the signup screen
# class SignupPage:
#     def __init__(self, page: ft.Page, app):
#         self.page = page
#         self.app = app
#         self.username_field = ft.TextField(label="Username")
#         self.password_field = ft.TextField(label="Password", password=True)
#         self.confirm_password_field = ft.TextField(label="Confirm Password", password=True)
#         self.init_ui()

#     def init_ui(self):
#         self.page.clean()
#         self.page.add(
#             ft.Column(
#                 controls=[
#                     ft.Text("Sign Up Page"),
#                     self.username_field,
#                     self.password_field,
#                     self.confirm_password_field,
#                     ft.ElevatedButton(text="Sign Up", on_click=self.signup),
#                     ft.ElevatedButton(text="Back to Login", on_click=self.app.show_login_page)
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#             )
#         )
#         self.page.update()

#     def signup(self, e):
#         username = self.username_field.value.strip()
#         password = self.password_field.value.strip()
#         confirm_password = self.confirm_password_field.value.strip()

#         # Check username policy (example: length between 3 and 20 characters)
#         if len(username) < 3 or len(username) > 20:
#             self.app.result.value = "Username must be between 3 and 20 characters."
#             self.page.update()
#             return
        
#         # Check password policy (example: length at least 8 characters)
#         if len(password) < 8:
#             self.app.result.value = "Password must be at least 8 characters."
#             self.page.update()
#             return
        
#         # Check if passwords match
#         if password != confirm_password:
#             self.app.result.value = "Passwords do not match."
#             self.page.update()
#             return

#         # Implement actual signup logic here (e.g., send request to server)
#         response = requests.post("http://127.0.0.1:8000/signup", json={"username": username, "password": password})
#         if response.status_code == 200:
#             self.app.result.value = "Signup successful"
#             # Clear the fields after successful signup
#             self.username_field.value = ""
#             self.password_field.value = ""
#             self.confirm_password_field.value = ""
#             self.app.show_login_page()  # Navigate back to login page
#         else:
#             self.app.result.value = "Signup failed. Please try again."
        
#         self.page.update()


# class SignupPage:
#     def __init__(self, page: ft.Page, app):
#         self.page = page
#         self.app = app
#         self.username_field = ft.TextField(label="Username")
#         self.password_field = ft.TextField(label="Password", password=True)
#         self.confirm_password_field = ft.TextField(label="Confirm Password", password=True)
#         self.init_ui()

#     def init_ui(self):
#         self.page.clean()
#         self.page.add(
#             ft.Column(
#                 controls=[
#                     ft.Text("Sign Up Page"),
#                     self.username_field,
#                     self.password_field,
#                     self.confirm_password_field,
#                     ft.ElevatedButton(text="Sign Up", on_click=self.signup),
#                     ft.ElevatedButton(text="Back to Login", on_click=self.app.show_login_page)
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#             )
#         )
#         self.page.update()

#     def signup(self, e):
#         username = self.username_field.value.strip()
#         password = self.password_field.value.strip()
#         confirm_password = self.confirm_password_field.value.strip()

#         # Check username policy (example: length between 3 and 20 characters)
#         if len(username) < 3 or len(username) > 20:
#             self.app.result.value = "Username must be between 3 and 20 characters."
#             self.page.update()
#             return
        
#         # Check password policy (example: length at least 8 characters)
#         if len(password) < 8:
#             self.app.result.value = "Password must be at least 8 characters."
#             self.page.update()
#             return
        
#         # Check if passwords match
#         if password != confirm_password:
#             self.app.result.value = "Passwords do not match."
#             self.page.update()
#             return

#         # Implement actual signup logic here (e.g., send request to server)
#         response = requests.post("http://127.0.0.1:8000/signup", json={"username": username, "password": password})
#         if response.status_code == 200:
#             self.app.result.value = "Signup successful"
#             # Clear the fields after successful signup
#             self.username_field.value = ""
#             self.password_field.value = ""
#             self.confirm_password_field.value = ""
#             self.app.show_login_page()  # Navigate back to login page
#         else:
#             self.app.result.value = "Signup failed. Please try again."
        
#         self.page.update()

class SignupPage:
    def __init__(self, page: ft.Page, app):
        self.page = page
        self.app = app
        self.username_field = ft.TextField(label="Username")
        self.password_field = ft.TextField(label="Password", password=True)
        self.confirm_password_field = ft.TextField(label="Confirm Password", password=True)
        self.init_ui()

    def init_ui(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                controls=[
                    ft.Text("Sign Up Page"),
                    self.username_field,
                    self.password_field,
                    self.confirm_password_field,
                    ft.ElevatedButton(text="Sign Up", on_click=self.signup),
                    ft.ElevatedButton(text="Back to Login", on_click=self.app.show_login_page)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.page.update()

    def signup(self, e):
        username = self.username_field.value.strip()
        password = self.password_field.value.strip()
        confirm_password = self.confirm_password_field.value.strip()

        try:
            # Check username policy (example: length between 3 and 20 characters)
            if len(username) < 3 or len(username) > 20:
                self.app.result.value = "Username must be between 3 and 20 characters."
                raise ValueError("")
            
            # Check password policy (example: length at least 8 characters)
            if len(password) < 8:
                self.app.result.value = "Password must be at least 8 characters."
                self.page.update()
                raise ValueError("")
            
            # Check if passwords match
            if password != confirm_password:
                self.app.result.value = "Passwords do not match."
                self.page.update()
                raise ValueError("")
            
            # Implement actual signup logic here (e.g., send request to server)
            response = requests.post("http://127.0.0.1:8000/signup", json={"username": username, "password": password})
            if response.status_code == 200:
                self.app.result.value = "Signup successful"
                # Clear the fields after successful signup
                self.username_field.value = ""
                self.password_field.value = ""
                self.confirm_password_field.value = ""
                self.app.show_login_page()  # Navigate back to login page
            else:
                self.app.result.value = "Signup failed. Please try again."
            
        except:
            self.page.update()

        self.page.update()



# PlotDataPage class to display the plot data
class PlotDataPage:
    def __init__(self, page: ft.Page, app):
        self.page = page
        self.app = app
        self.init_ui()

    def init_ui(self):
        fig = plotly.create_chart()
        plot = PlotlyChart(fig)
        self.page.clean()
        self.page.add(
            ft.Column(
                controls=[
                    ft.ElevatedButton(text="Back to Welcome Page", on_click=self.app.show_welcome_page),
                    plot
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.page.update()

# # Main application class to manage the different pages and states
# class DashboardApp:
#     def __init__(self, page: ft.Page):
#         self.page = page
#         self.page.title = "ChatGPT App"
#         self.is_logged_in = False
#         self.result = ft.Text()

#         self.username_field = ft.TextField(label="Username")
#         self.password_field = ft.TextField(label="Password", password=True)

#         self.show_welcome_page()

#     # Method to show the welcome page
#     def show_welcome_page(self, e=None):
#         self.welcome_page = WelcomePage(self.page, self)

#     # Method to show the login page
#     def show_login_page(self, e=None):
#         self.page.clean()
#         self.page.add(
#             ft.Column(
#                 controls=[
#                     ft.Text("Login Page"),
#                     self.username_field,
#                     self.password_field,
#                     ft.ElevatedButton(text="Login", on_click=self.login),
#                     ft.ElevatedButton(text="Sign Up", on_click=self.show_signup_page)
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#             )
#         )
#         self.page.update()

#     # Method to show the signup page
#     def show_signup_page(self, e=None):
#         self.signup_page = SignupPage(self.page, self)

#     # Method to handle the login logic
#     def login(self, e):
#         username = self.username_field.value
#         password = self.password_field.value

#         response = requests.post("http://127.0.0.1:8000/login", json={"username": username, "password": password})
#         if response.status_code == 200:
#             self.is_logged_in = True
#             self.result.value = "Login successful"
#             self.show_dashboard_page()
#         else:
#             self.result.value = "Login failed"
#         self.page.update()

#     # Method to show the dashboard page
#     def show_dashboard_page(self, e=None):
#         if not hasattr(self, 'dashboard_page'):
#             self.dashboard_page = DashboardPage(self.page, self)
#         self.dashboard_page.init_ui()

#     # Method to show the plot data page
#     def show_plot_data_page(self, e=None):
#         self.plot_data_page = PlotDataPage(self.page, self)

#     # # Method to handle the logout logic
#     # def logout(self, e):
#     #     self.is_logged_in = False
#     #     self.result.value = ""
#     #     self.username_field = ft.TextField(label="Username")
#     #     self.password_field = ft.TextField(label="Password", password=True)
#     #     self.show_welcome_page()

#     # Method to handle the logout logic
#     def logout(self, e):
#         self.is_logged_in = False
#         self.result.value = ""
#         self.username_field = ft.TextField(label="Username")
#         self.password_field = ft.TextField(label="Password", password=True)
#         self.show_login_page()  # Show the login page after logout

# # Main function to run the app
# def main(page: ft.Page):
#     app = DashboardApp(page)

# ft.app(target=main)


# Main application class to manage the different pages and states
class DashboardApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "ChatGPT App"
        self.is_logged_in = False
        self.result = ft.Text()

        self.username_field = ft.TextField(label="Username")
        self.password_field = ft.TextField(label="Password", password=True)

        self.show_welcome_page()

    # Method to show the welcome page
    def show_welcome_page(self, e=None):
        self.welcome_page = WelcomePage(self.page, self)

    # Method to show the login page
    def show_login_page(self, e=None):
        self.page.clean()
        self.page.add(
            ft.Column(
                controls=[
                    ft.Text("Login Page"),
                    self.username_field,
                    self.password_field,
                    ft.ElevatedButton(text="Login", on_click=self.login),
                    ft.ElevatedButton(text="Sign Up", on_click=self.show_signup_page)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.page.update()

    # Method to show the signup page
    def show_signup_page(self, e=None):
        self.signup_page = SignupPage(self.page, self)

    # Method to handle the login logic
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

    # Method to show the dashboard page
    def show_dashboard_page(self, e=None):
        if not hasattr(self, 'dashboard_page'):
            self.dashboard_page = DashboardPage(self.page, self)
        self.dashboard_page.init_ui()

    # Method to show the plot data page
    def show_plot_data_page(self, e=None):
        self.plot_data_page = PlotDataPage(self.page, self)

    # Method to handle the logout logic
    def logout(self, e):
        self.is_logged_in = False
        self.result.value = ""
        self.username_field = ft.TextField(label="Username")
        self.password_field = ft.TextField(label="Password", password=True)
        self.show_login_page()  # Show the login page after logout

# Main function to run the app
def main(page: ft.Page):
    app = DashboardApp(page)

ft.app(target=main)
