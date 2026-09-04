from playwright.sync_api import Page


class ContractsPage:
    def __init__(self, page: Page):
        self.page = page

        self.contracts_link = page.get_by_role(
            "link",
            name="Contracts",
            exact=True
        )

        self.active_contracts = page.get_by_role(
            "cell",
            name="ACTIVE",
            exact=True
        )

        self.breadcrumb = page.get_by_label("Breadcrumb")

        self.breadcrumb_contracts_link = self.breadcrumb.get_by_role(
            "link",
            name="Contracts",
            exact=True
        )

    def open_contracts(self) -> None:
        self.contracts_link.click()

    def open_first_active_contract(self) -> None:
        self.active_contracts.first.click()

    def back_to_contracts(self) -> None:
        self.breadcrumb_contracts_link.click()