from playwright.sync_api import Page, expect


class ContractsPage:
    """Page object for the Client Contracts page."""

    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.contracts_link = page.get_by_role(
            "link",
            name="Contracts",
            exact=True
        )

        # Contract page
        self.technician_text = page.get_by_text(
            "Technician",
            exact=True
        )

        # Contract
        self.bkt_contract = page.get_by_role(
            "cell",
            name="Bkt",
            exact=True
        )

    def open_contracts(self) -> None:
        self.contracts_link.click()

    def verify_technician_visible(self) -> None:
        expect(self.technician_text).to_be_visible()

    def open_bkt_contract(self) -> None:
        self.bkt_contract.click()