from playwright.sync_api import Page


class AdminProposalsPage:
    def __init__(self, page: Page):
        self.page = page

        self.proposals_link = page.get_by_role(
            "link",
            name="Proposals",
            exact=True
        )

        self.proposals_breadcrumb = (
            page.get_by_label("Breadcrumb")
            .get_by_role(
                "link",
                name="Proposals"
            )
        )

    def click_proposals(self) -> None:
        self.proposals_link.click()

    def open_proposal(self, proposal_name: str) -> None:
        self.page.get_by_role(
            "cell",
            name=proposal_name
        ).click()

    def back_to_proposals(self) -> None:
        self.proposals_breadcrumb.click()




