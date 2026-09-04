
from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object for the EscapePlan Admin Login page."""

    def __init__(self, page: Page):
        self.page = page

        self.email_input = page.get_by_role(
            "textbox",
            name="admin@escapeplan.com"
        )

        self.password_input = page.get_by_role(
            "textbox",
            name="••••••••"
        )

        self.sign_in_button = page.get_by_role(
            "button",
            name="Sign In"
        )

    def enter_email(self, email: str) -> None:
        # self.email_input.click()
        self.email_input.fill(email)

    def enter_password(self, password: str) -> None:
        # self.password_input.click()
        self.password_input.fill(password)

    def click_sign_in(self) -> None:
        self.sign_in_button.click()

    def login(self, email: str, password: str) -> None:
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in()

