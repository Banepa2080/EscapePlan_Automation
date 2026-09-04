from playwright.sync_api import Page


class Admin_AddUser:

    def __init__(self, page: Page):
        self.page = page

        self.add_user_link = page.get_by_role(
            "link",
            name="Add User"
        )

    def click_add_user(self) -> None:
        self.add_user_link.click()


