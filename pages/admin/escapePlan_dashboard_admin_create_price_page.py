from playwright.sync_api import Page


class AdminCreatePricingPage:

    def __init__(self, page: Page):
        self.page = page

        self.pricing_link = page.get_by_role(
            "link",
            name="Pricing",
            exact=True
        )

        self.add_plan_link = page.get_by_role(
            "link",
            name="Add Plan"
        )

        self.plan_name_input = page.get_by_role(
            "textbox",
            name="Basic Plan"
        )

        self.price_input = page.get_by_placeholder(
            "99"
        )

        # self.currency_select = (
        #     page.locator("div")
        #     .filter(has_text="CurrencyEURUSDGBP")
        #     .get_by_role("combobox")
        # )

        # self.type_select = (
        #     page.locator("div")
        #     .filter(has_text="TypeOne TimeRecurringSubscription")
        #     .get_by_role("combobox")
        # )

        

        self.create_plan_button = page.get_by_role(
            "button",
            name="Create Plan"
        )

    def click_pricing(self) -> None:
        self.pricing_link.click()

    def click_add_plan(self) -> None:
        self.add_plan_link.click()

    def enter_plan_name(self, plan_name: str) -> None:
        self.plan_name_input.fill(plan_name)

    def enter_price(self, price: str) -> None:
        self.price_input.fill(price)

    # def select_currency(self, currency: str) -> None:
    #     self.currency_select.select_option(currency)

    # def select_plan_type(self, plan_type: str) -> None:
    #     self.type_select.select_option(plan_type)
    

    def click_create_plan(self) -> None:
        self.create_plan_button.click()