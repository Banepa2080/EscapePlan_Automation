from playwright.sync_api import Page


class AdminCreateAdminPage:

    def __init__(self, page: Page):
        self.page = page

        self.admin_users_link = page.get_by_role(
            "link",
            name="Admin Users"
        )

        self.add_admin_link = page.get_by_role(
            "link",
            name="Add Admin"
        )

        self.name_input = page.get_by_role(
            "textbox",
            name="e.g. John Smith"
        )

        self.email_input = page.get_by_role(
            "textbox",
            name="admin@escapeplan.com"
        )

        self.role_select = page.get_by_role(
            "combobox"
        )

        self.generate_password_button = page.get_by_role(
            "button",
            name="Generate Password"
        )

        self.send_invitation_checkbox = page.get_by_role(
            "checkbox",
            name="Send invitation email with"
        )

        self.create_admin_button = page.get_by_role(
            "button",
            name="Create Admin"
        )

    def click_admin_users(self) -> None:
        self.admin_users_link.click()

    def click_add_admin(self) -> None:
        self.add_admin_link.click()

    def enter_name(self, name: str) -> None:
        self.name_input.fill(name)

    def enter_email(self, email: str) -> None:
        self.email_input.fill(email)

    def select_role(self, role: str) -> None:
        self.role_select.select_option(role)

    def generate_password(self) -> None:
        self.generate_password_button.click()

    def enable_invitation_email(self) -> None:
        self.send_invitation_checkbox.check()

    def click_create_admin(self) -> None:
        self.create_admin_button.click()