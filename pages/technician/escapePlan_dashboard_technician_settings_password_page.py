from playwright.sync_api import Page


class TechnicianPasswordChangePage:
    def __init__(self, page: Page):
        self.page = page

        self.settings_link = page.get_by_role(
            "link",
            name="Settings"
        )

        self.password_change_button = page.get_by_role(
            "button",
            name="Password Change your password"
        )

        self.current_password_input = page.get_by_role(
            "textbox",
            name="Enter current password"
        )

        self.new_password_input = page.get_by_role(
            "textbox",
            name="Min. 6 characters"
        )

        self.confirm_password_input = page.get_by_role(
            "textbox",
            name="Re-enter new password"
        )

        self.update_password_button = page.get_by_role(
            "button",
            name="Update Password"
        )

    def click_settings(self) -> None:
        self.settings_link.click()

    def open_password_change(self) -> None:
        self.password_change_button.click()

    def enter_current_password(self, password: str) -> None:
        self.current_password_input.fill(password)

    def enter_new_password(self, password: str) -> None:
        self.new_password_input.fill(password)

    def confirm_new_password(self, password: str) -> None:
        self.confirm_password_input.fill(password)

    def update_password(self) -> None:
        self.update_password_button.click()

    def change_password(
        self,
        current_password: str,
        new_password: str,
    ) -> None:
        self.click_settings()
        self.open_password_change()
        self.enter_current_password(current_password)
        self.enter_new_password(new_password)
        self.confirm_new_password(new_password)
        self.update_password()