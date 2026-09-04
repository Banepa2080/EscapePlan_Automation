from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

        self.dashboard_link = page.get_by_role(
            "link",
            name="Dashboard",
            exact=True
        )

        self.browse_available_jobs_link = page.get_by_role(
            "link",
            name="Browse Available Jobs",
            exact=True
        )

    def open_dashboard(self) -> None:
        self.dashboard_link.click()

    def open_browse_available_jobs(self) -> None:
        self.browse_available_jobs_link.click()



class AvailableJobsPage:
    def __init__(self, page: Page):
        self.page = page

        self.job_rows = page.locator("tbody tr")

        self.breadcrumb = page.get_by_label("Breadcrumb")

        self.browse_jobs_link = self.breadcrumb.get_by_role(
            "link",
            name="Browse Jobs",
            exact=True
        )

    def open_first_job(self) -> None:
        self.job_rows.first.click()

    def back_to_browse_jobs(self) -> None:
        self.browse_jobs_link.click()