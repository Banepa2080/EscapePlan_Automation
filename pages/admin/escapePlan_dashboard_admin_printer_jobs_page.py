from playwright.sync_api import Page


class AdminPrinterJobsPage:

    def __init__(self, page: Page):
        self.page = page

        self.printer_jobs_link = page.get_by_role(
            "link",
            name="Printer Jobs"
        )

        self.job_title_text = page.get_by_text(
            "Job Title"
        )

        self.printer_job_cells = page.get_by_role(
            "cell",
            name="printer job"
        )

    def click_printer_jobs(self) -> None:
        self.printer_jobs_link.click()

    def is_job_title_visible(self) -> bool:
        return self.job_title_text.is_visible()

    def click_printer_job(self, index: int = 2) -> None:
        self.printer_job_cells.nth(index).click()