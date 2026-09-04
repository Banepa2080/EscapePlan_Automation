# from playwright.sync_api import Page


# class Admin_AddUser:

#     def __init__(self, page: Page):
#         self.page = page

#         self.add_user_link = page.get_by_role(
#             "link",
#             name="Add User"
#         )

#     def click_add_user(self) -> None:
#         self.add_user_link.click()


from playwright.sync_api import Page


class AdminCreateUserPage:
    def __init__(self, page: Page):
        self.page = page

        self.users_link = page.get_by_role(
            "link",
            name="Users",
            exact=True
        )

        self.add_user_button = page.get_by_role(
            "button",
            name="Add User"
        )

        self.name_input = page.get_by_role(
            "textbox",
            name="John Doe"
        )

        self.email_input = page.get_by_role(
            "textbox",
            name="john@example.com"
        )

        self.password_input = page.get_by_role(
            "textbox",
            name="Minimum 8 characters"
        )

        self.role_select = page.locator("form").get_by_role(
            "combobox"
        )

        self.create_user_button = page.get_by_role(
            "button",
            name="Create User"
        )

    def click_users(self) -> None:
        self.users_link.click()

    def click_add_user(self) -> None:
        self.add_user_button.click()

    def enter_name(self, name: str) -> None:
        self.name_input.fill(name)

    def enter_email(self, email: str) -> None:
        self.email_input.fill(email)

    def enter_password(self, password: str) -> None:
        self.password_input.fill(password)

    def select_role(self, role: str) -> None:
        self.role_select.select_option(role)

    def click_create_user(self) -> None:
        self.create_user_button.click()

    def create_user(
        self,
        name: str,
        email: str,
        password: str,
        role: str,
    ) -> None:
        self.click_users()
        self.click_add_user()
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.select_role(role)
        self.click_create_user()