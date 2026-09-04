from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

        self.dashboard_link = page.get_by_role(
            "link",
            name="Dashboard",
            exact=True
        )

        self.view_printer_jobs_link = page.get_by_role(
            "link",
            name="View Printer Jobs",
            exact=True
        )

    def open_dashboard(self) -> None:
        self.dashboard_link.click()

    def open_view_printer_jobs(self) -> None:
        self.view_printer_jobs_link.click()


