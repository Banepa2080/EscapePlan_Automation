from playwright.sync_api import Page


class AdminDashboardPage:
    def __init__(self, page: Page):
        self.page = page

        self.dashboard_link = page.get_by_role(
            "link",
            name="Dashboard"
        )

        self.users_link = page.get_by_role(
            "link",
            name="53 Users"
        )

        self.proposals_link = page.get_by_role(
            "link",
            name="29 Proposals"
        )

        self.reviews_pending_link = page.get_by_role(
            "link",
            name="Reviews Pending"
        )

        self.printers_link = page.get_by_role(
            "link",
            name="Printers"
        )

        self.technicians_link = page.get_by_role(
            "link",
            name="11 Technicians"
        )

        self.pricing_plans_link = page.get_by_role(
            "link",
            name="21 Pricing Plans"
        )

        self.user_cell = page.get_by_role(
            "cell",
            name="full name test"
        )

        self.proposal_cell = page.get_by_role(
            "cell",
            name="Automated job title"
        )

        self.review_cell = page.get_by_role(
            "cell",
            name="Floor Plan Markup"
        )

        self.printer_cell = page.get_by_role(
            "cell",
            name="sita",
            exact=True
        )

      

    def click_dashboard(self) -> None:
        self.dashboard_link.click()

    def open_users(self) -> None:
        self.users_link.click()

    def open_user(self, user_name: str) -> None:
        self.page.get_by_role(
            "cell",
            name=user_name
        ).first.click()

    def back_to_users(self) -> None:
        self.page.get_by_label(
            "Breadcrumb"
        ).get_by_role(
            "link",
            name="Users"
        ).click()

    def open_proposals(self) -> None:
        self.proposals_link.click()

    def open_proposal(self, proposal_name: str) -> None:
        self.page.get_by_role(
            "cell",
            name=proposal_name
        ).click()

    def back_to_proposals(self) -> None:
        self.page.get_by_label(
            "Breadcrumb"
        ).get_by_role(
            "link",
            name="Proposals"
        ).click()

    def open_pending_reviews(self) -> None:
        self.reviews_pending_link.click()

    def open_review(self, review_name: str) -> None:
        self.page.get_by_role(
            "cell",
            name=review_name
        ).click()

    def back_to_reviews(self) -> None:
        self.page.get_by_role(
            "link",
            name="Back to Reviews"
        ).click()

    def open_printers(self) -> None:
        self.printers_link.click()

    def open_printer(self, printer_name: str) -> None:
        self.page.get_by_role(
            "cell",
            name=printer_name,
            exact=True
        ).click()

    def open_technicians(self) -> None:
        self.technicians_link.click()

    def open_technician(self, technician_name: str) -> None:
        self.page.get_by_role(
            "cell",
            name=technician_name
        ).first.click()

    def back_to_technicians(self) -> None:
        self.page.get_by_label(
            "Breadcrumb"
        ).get_by_role(
            "link",
            name="Technicians"
        ).click()

    def open_pricing_plans(self) -> None:
        self.pricing_plans_link.click()

    # def open_first_pricing_plan(self) -> None:
    def open_pricing_plan(self, Basic_Plan: str) -> None:
        self.page.get_by_role(
            "cell",
            name=Basic_Plan
        # ).click()
        ).first.click()

    def back_to_pricing_plans(self) -> None:
        self.page.get_by_label(
            "Breadcrumb"
        ).get_by_role(
            "link",
            name="Pricing Plans"
        ).click()
    