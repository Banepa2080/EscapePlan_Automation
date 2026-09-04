from playwright.sync_api import Page


class ClientDashboardPage:
    def __init__(self, page: Page):
        self.page = page

        self.dashboard_link = page.get_by_role(
            "link", name="Dashboard", exact=True
        )

        self.my_buildings_link = page.get_by_role(
            "link", name="19 My Buildings", exact=True
        )

        self.active_jobs_link = page.get_by_role(
            "link", name="— Active Jobs"
        )

        self.proposals_link = page.get_by_role(
            "link", name="2 Proposals"
        )

        self.buildings_breadcrumb = (
            page.get_by_label("Breadcrumb")
            .get_by_role("link", name="Buildings", exact=True)
        )

        self.jobs_breadcrumb = (
            page.get_by_label("Breadcrumb")
            .get_by_role("link", name="Jobs", exact=True)
        )

        self.back_link = page.get_by_role(
            "link", name="Back", exact=True
        )

    def click_dashboard(self) -> None:
        self.dashboard_link.click()

    def open_my_buildings(self) -> None:
        self.my_buildings_link.click()

    def open_building(self, building_name: str) -> None:
        self.page.get_by_text(
            building_name,
            exact=True
        ).click()

    def back_to_buildings(self) -> None:
        self.buildings_breadcrumb.click()

    def open_active_jobs(self) -> None:
        self.active_jobs_link.click()

    def open_job(self, job_title: str) -> None:
        self.page.get_by_text(
            job_title,
            exact=True
        ).click()

    def back_to_jobs(self) -> None:
        self.jobs_breadcrumb.click()

    def open_proposals(self) -> None:
        self.proposals_link.click()

    def open_proposal(self, job_title: str) -> None:
        self.page.get_by_role(
            "cell",
            name=job_title,
            exact=True
        ).click()

    def go_back(self) -> None:
        self.back_link.click()