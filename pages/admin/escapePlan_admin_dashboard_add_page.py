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



class Admin_AddTemplate:

    def __init__(self, page: Page):
        self.page = page

        self.add_template_link = page.get_by_role(
            "link",
            name="Add Template"
        )

    def click_add_template(self) -> None:
        self.add_template_link.click()

class Admin_AddSymbol:

    def __init__(self, page: Page):
        self.page = page

        self.add_symbol_link = page.get_by_role(
            "link",
            name="Add Symbol"
        )

    def click_add_symbol(self) -> None:
        self.add_symbol_link.click()

class Admin_AddPricing:

    def __init__(self, page: Page):
        self.page = page

        self.add_pricing_link = page.get_by_role(
            "link",
            name="Add Pricing Plan"
        )

    def click_add_pricing(self) -> None:
        self.add_pricing_link.click()


