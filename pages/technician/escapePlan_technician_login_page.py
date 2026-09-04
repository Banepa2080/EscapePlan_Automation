from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object for EscapePlan Login page."""

    def __init__(self, page: Page):
        self.page = page

        self.username_input = page.get_by_role(
            "textbox",
            name="you@example.com"
        )

        self.password_input = page.get_by_role(
            "textbox",
            name="••••••••"
        )

        self.login_button = page.get_by_role(
            "button",
            name="Sign In"
        )

        # Adjust these locators according to the actual application.
        self.login_error = page.get_by_text(
            "Invalid email or password",
            exact=False
        )

    def navigate_to_login(self):
        self.page.goto(
            "https://staging-v2-dash.escapeplan.ie/login"
        )

    def enter_email(self, username: str):
        self.username_input.fill(username)

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username: str, password: str):
        self.enter_email(username)
        self.enter_password(password)
        self.click_login()

    def is_login_button_visible(self):
        return self.login_button.is_visible()
