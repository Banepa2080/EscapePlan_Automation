from playwright.sync_api import Page

class LoginPage:
    """Page Object for EscapePlan Login page."""

    def __init__(self, page:Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="you@example.com")
        self.password_input = page.get_by_role("textbox", name="••••••••")
        self.login_button = page.get_by_role("button", name="Sign In")

    def enter_emailAddress(self, username:str):
        self.username_input.fill(username)

    def enter_password(self, password:str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username:str, password:str):
        self.enter_emailAddress(username)
        self.enter_password(password)
        self.click_login()