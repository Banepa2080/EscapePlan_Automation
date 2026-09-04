from playwright.sync_api import Page


class TechnicianMyProposalsPage:
    def __init__(self, page: Page):
        self.page = page

        self.my_proposals_link = page.get_by_role(
            "link",
            name="My Proposals",
            exact=True
        )

        self.proposal_rows = page.locator("tbody tr")

        self.breadcrumb = page.get_by_label("Breadcrumb")

        self.breadcrumb_my_proposals_link = self.breadcrumb.get_by_role(
            "link",
            name="My Proposals",
            exact=True
        )

    def open_my_proposals(self) -> None:
        self.my_proposals_link.click()

    def open_first_proposal(self) -> None:
        self.proposal_rows.first.click()

    def back_to_my_proposals(self) -> None:
        self.breadcrumb_my_proposals_link.click()