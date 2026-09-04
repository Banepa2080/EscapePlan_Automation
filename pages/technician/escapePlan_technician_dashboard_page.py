from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

        self.dashboard_link = page.get_by_role(
            "link", name="Dashboard", exact=True
        )

        self.available_jobs_link = page.get_by_role(
            "link", name="— Available Jobs"
        )

        self.active_jobs_link = page.get_by_role(
            "link", name="Active Jobs"
        )

        self.proposals_sent_link = page.get_by_role(
            "link", name="Proposals Sent"
        )

    def open_dashboard(self) -> None:
        self.dashboard_link.click()

    def open_available_jobs(self) -> None:
        self.available_jobs_link.click()

    def open_active_jobs(self) -> None:
        self.active_jobs_link.click()

    def open_proposals_sent(self) -> None:
        self.proposals_sent_link.click()




class AvailableJobsPage:
    def __init__(self, page: Page):
        self.page = page

        self.breadcrumb = page.get_by_label("Breadcrumb")

        self.job_cells = page.locator("tbody tr")

    def open_first_job(self) -> None:
        self.job_cells.first.click()

    def back_to_browse_jobs(self) -> None:
        self.breadcrumb.get_by_role(
            "link", name="Browse Jobs"
        ).click()



class ActiveJobsPage:
    def __init__(self, page: Page):
        self.page = page

        self.breadcrumb = page.get_by_label("Breadcrumb")
        self.job_rows = page.locator("tbody tr")

    def open_first_active_job(self) -> None:
        self.job_rows.first.click()

    def back_to_my_jobs(self) -> None:
        self.breadcrumb.get_by_role(
            "link", name="My Jobs"
        ).click()


class ProposalsPage:
    def __init__(self, page: Page):
        self.page = page

        self.breadcrumb = page.get_by_label("Breadcrumb")
        self.proposal_rows = page.locator("tbody tr")

    def open_first_proposal(self) -> None:
        self.proposal_rows.first.click()

    def back_to_my_proposals(self) -> None:
        self.breadcrumb.get_by_role(
            "link", name="My Proposals"
        ).click()