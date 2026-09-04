
from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        # Navigation links
        self.dashboard_link = page.get_by_role("link", name="Dashboard")
        self.printer_jobs_link = page.get_by_role(
            "link", name="— Printer Jobs"
        )
        self.my_clients_link = page.get_by_role(
            "link", name="— My Clients"
        )

    def go_to_dashboard(self) -> None:
        self.dashboard_link.click()

    def go_to_printer_jobs(self) -> None:
        self.printer_jobs_link.click()

    def go_to_my_clients(self) -> None:
        self.my_clients_link.click()

