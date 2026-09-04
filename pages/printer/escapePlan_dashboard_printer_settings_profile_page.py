from playwright.sync_api import Page


class PrinterProfileSettingsPage:
    def __init__(self, page: Page):
        self.page = page

        self.settings_link = page.get_by_role(
            "link",
            name="Settings"
        )

        self.profile_button = page.get_by_role(
            "button",
            name="Profile Personal & contact"
        )

        self.full_name_input = page.get_by_role(
            "textbox",
            name="Your full name"
        )

        self.phone_input = page.get_by_role(
            "textbox",
            name="+1 (555) 000-"
        )

        self.company_input = page.get_by_role(
            "textbox",
            name="Your company (optional)"
        )

        self.address_input = page.get_by_role(
            "textbox",
            name="Main St"
        )

        self.city_input = page.get_by_role(
            "textbox",
            name="City"
        )

        self.postcode_input = page.get_by_role(
            "textbox",
            name="12345"
        )

        self.country_input = page.get_by_role(
            "textbox",
            name="United States"
        )

        self.save_changes_button = page.get_by_role(
            "button",
            name="Save Changes"
        )

    def click_settings(self) -> None:
        self.settings_link.click()

    def open_profile(self) -> None:
        self.profile_button.click()

    def enter_full_name(self, full_name: str) -> None:
        self.full_name_input.fill(full_name)

    def enter_phone(self, phone: str) -> None:
        self.phone_input.fill(phone)

    def enter_company(self, company: str) -> None:
        self.company_input.fill(company)

    def enter_address(self, address: str) -> None:
        self.address_input.fill(address)

    def enter_city(self, city: str) -> None:
        self.city_input.fill(city)

    def enter_postcode(self, postcode: str) -> None:
        self.postcode_input.fill(postcode)

    def enter_country(self, country: str) -> None:
        self.country_input.fill(country)

    def save_changes(self) -> None:
        self.save_changes_button.click()

    def update_profile(
        self,
        full_name: str,
        phone: str,
        company: str,
        address: str,
        city: str,
        postcode: str,
        country: str,
    ) -> None:
        self.click_settings()
        self.open_profile()
        self.enter_full_name(full_name)
        self.enter_phone(phone)
        self.enter_company(company)
        self.enter_address(address)
        self.enter_city(city)
        self.enter_postcode(postcode)
        self.enter_country(country)
        self.save_changes()