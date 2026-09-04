from playwright.sync_api import Page


class TechnicianBrowseJobsPage:
    """Page object for a technician browsing jobs and submitting a proposal."""

    def __init__(self, page: Page):
        self.page = page
        self.browse_jobs_link = page.get_by_role("link", name="Browse Jobs")
        self.submit_proposal_link = page.get_by_role(
            "link", name="Submit Proposal"
        ).first
        self.expertise_input = page.get_by_role(
            "textbox", name="e.g. Fire Safety Expert"
        )
        self.estimated_days_input = page.get_by_role("spinbutton")
        self.proposed_cost_input = page.get_by_role("textbox", name="$")
        self.start_date_input = page.locator('input[type="date"]').nth(0)
        self.end_date_input = page.locator('input[type="date"]').nth(1)
        self.approach_input = page.get_by_role(
            "textbox", name="Describe your approach..."
        )
        self.risks_input = page.get_by_role(
            "textbox", name="Identify potential risks..."
        )
        self.design_strategy_input = page.get_by_role(
            "textbox", name="Your design strategy..."
        )
        self.notes_input = page.locator("textarea").nth(3)
        self.submit_proposal_button = page.get_by_role(
            "button", name="Submit Proposal"
        )

    def open_browse_jobs(self) -> None:
        self.browse_jobs_link.click()

    def has_available_jobs(self) -> bool:
        job_cells = self.page.get_by_role("cell")
        return (
            job_cells.count() > 0
            and "no job" not in job_cells.first.inner_text().lower()
        )

    def open_first_available_job(self) -> None:
        self.page.get_by_role("cell").first.click()

    def open_proposal_form(self) -> None:
        self.submit_proposal_link.click()

    def fill_proposal(
        self,
        expertise: str,
        estimated_days: str,
        proposed_cost: str,
        start_date: str,
        end_date: str,
        approach: str,
        risks: str,
        design_strategy: str,
        notes: str,
    ) -> None:
        self.expertise_input.fill(expertise)
        self.estimated_days_input.fill(estimated_days)
        self.proposed_cost_input.fill(proposed_cost)
        self.start_date_input.fill(start_date)
        self.end_date_input.fill(end_date)
        self.approach_input.fill(approach)
        self.risks_input.fill(risks)
        self.design_strategy_input.fill(design_strategy)
        self.notes_input.fill(notes)

    def submit_proposal(self) -> None:
        self.submit_proposal_button.click()

    def submit_job_proposal(self, **proposal: str) -> None:
        self.open_browse_jobs()
        self.open_first_available_job()
        self.open_proposal_form()
        self.fill_proposal(**proposal)
        self.submit_proposal()
