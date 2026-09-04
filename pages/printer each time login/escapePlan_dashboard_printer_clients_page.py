from playwright.sync_api import Page


class PrinterClientsPage:
    def __init__(self, page: Page):
        self.page = page

        self.clients_link = page.get_by_role(
            "link",
            name="Clients",
            exact=True
        )

    def open_clients(self) -> None:
        self.clients_link.click()