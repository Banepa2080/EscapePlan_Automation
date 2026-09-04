import re

from playwright.sync_api import Page


class ClientProposalsPage:
    """Page object for navigating and managing client proposals."""

    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.proposals_link = page.get_by_role(
            "link",
            name="Proposals",
            exact=True,
        )

        self.job_2_proposals_link = page.get_by_role(
            "link",
            name="Job 2 proposals received",
        )

        # Job proposals page
        self.proposal_status = page.get_by_text(
            re.compile(r"ACCEPT|PENDING", re.I)
        )

        # "details" shown on the proposal card
        self.proposal_details = page.get_by_text(
            "details",
            exact=True,
        )

        # Final proposal page
        self.accept_proposal_button = page.get_by_role(
            "button",
            name="Accept Proposal",
            exact=True,
        )

    def open_proposals(self) -> None:
        """Open the Proposals page."""
        self.proposals_link.click()

    def open_job_2_proposals(self) -> None:
        """Open proposals received for the job."""
        self.job_2_proposals_link.click()

    def verify_proposals_exist(self) -> None:
        """Verify that at least one proposal exists."""
        self.page.get_by_text(
            re.compile(r"\d+\s+proposal\(s\)", re.I)
        ).is_visible()

    def open_latest_proposal(self) -> None:
        """
        Open the first proposal without hard-coding
        proposal name or proposal ID.
        """
        self.proposal_status.first.click()

    def open_proposal_details(self) -> None:
        """Open the proposal details page."""
        self.proposal_details.first.click()

    def click_accept_proposal(self) -> None:
        """Accept the proposal."""
        self.accept_proposal_button.click()

    def accept_latest_proposal(self) -> None:
        """Open latest proposal and accept it."""
        self.open_latest_proposal()
        self.open_proposal_details()
        self.click_accept_proposal()