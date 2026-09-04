from playwright.sync_api import Page


class BrowseJobsPage:
    def __init__(self, page: Page):
        self.page = page

        self.browse_jobs_link = page.get_by_role(
            "link",
            name="Browse Jobs",
            exact=True
        )

        self.job_rows = page.locator("tbody tr")

        self.breadcrumb = page.get_by_label("Breadcrumb")

        self.breadcrumb_browse_jobs_link = self.breadcrumb.get_by_role(
            "link",
            name="Browse Jobs",
            exact=True
        )

    def open_browse_jobs(self) -> None:
        self.browse_jobs_link.click()

    def open_first_job(self) -> None:
        self.job_rows.first.click()

    def back_to_browse_jobs(self) -> None:
        self.breadcrumb_browse_jobs_link.click()