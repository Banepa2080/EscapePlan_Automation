from playwright.sync_api import Page


class PrinterHistoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.printer_history_link = page.get_by_role(
            "link",
            name="History",
            exact=True
        )

    def open_printer_history(self) -> None:
        self.printer_history_link.click()