# from playwright.sync_api import Page


# class AdminPDFReviewPage:
#     def __init__(self, page: Page):
#         self.page = page

#         self.pdf_review_link = page.get_by_role(
#             "link",
#             name="PDF Review"
#         )

#         self.evacuation_diagram_cell = page.get_by_role(
#             "cell",
#             name="Evacuation Diagram"
#         )

#         self.back_to_reviews_link = page.get_by_role(
#             "link",
#             name="Back to Reviews"
#         )

#         self.floor_plan_markup_cell = page.get_by_role(
#             "cell",
#             name="Floor Plan Markup"
#         )

#     def click_pdf_review(self) -> None:
#         self.pdf_review_link.click()

#     def open_evacuation_diagram(self) -> None:
#         self.evacuation_diagram_cell.click()

#     def back_to_reviews(self) -> None:
#         self.back_to_reviews_link.click()

#     def open_floor_plan_markup(self) -> None:
#         self.floor_plan_markup_cell.click()



from playwright.sync_api import Page


class AdminPDFReviewPage:
    def __init__(self, page: Page):
        self.page = page

        self.pdf_review_link = page.get_by_role(
            "link",
            name="PDF Review"
        )

        self.view_review_details_link = page.get_by_role(
            "link",
            name="View Review Details"
        )

        self.review_notes_input = page.get_by_role(
            "textbox",
            name="Write your review notes..."
        )

        self.submit_review_button = page.get_by_role(
            "button",
            name="Submit Review"
        )

        self.back_to_reviews_link = page.get_by_role(
            "link",
            name="Back to Reviews"
        )

    def click_pdf_review(self) -> None:
        self.pdf_review_link.click()

    def open_review(self, review_name: str) -> None:
        self.page.get_by_role(
            "cell",
            name=review_name
        ).click()

    def click_view_review_details(self) -> None:
        self.view_review_details_link.click()

    def enter_review_notes(self, notes: str) -> None:
        self.review_notes_input.fill(notes)

    def submit_review(self) -> None:
        self.submit_review_button.click()

    def back_to_reviews(self) -> None:
        self.back_to_reviews_link.click()