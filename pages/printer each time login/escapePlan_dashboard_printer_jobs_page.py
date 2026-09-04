from playwright.sync_api import Page


class PrinterJobsPage:
    def __init__(self, page: Page):
        self.page = page

        self.printer_jobs_link = page.get_by_role(
            "link",
            name="Printer Jobs",
            exact=True
        )

    def open_printer_jobs(self) -> None:
        self.printer_jobs_link.click()

   