from playwright.sync_api import Page


class TechnicianMyJobsPage:
    def __init__(self, page: Page):
        self.page = page

        self.my_jobs_link = page.get_by_role(
            "link",
            name="My Jobs",
            exact=True
        )

        self.job_rows = page.locator("tbody tr")

        self.breadcrumb = page.get_by_label("Breadcrumb")

        self.breadcrumb_my_jobs_link = self.breadcrumb.get_by_role(
            "link",
            name="My Jobs",
            exact=True
        )

    def open_my_jobs(self) -> None:
        self.my_jobs_link.click()

    def open_first_job(self) -> None:
        self.job_rows.first.click()

    def back_to_my_jobs(self) -> None:
        self.breadcrumb_my_jobs_link.click()