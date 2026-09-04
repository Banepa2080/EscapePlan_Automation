from playwright.sync_api import Page


class CompletePDFPage:
    def __init__(self, page: Page):
        self.page = page

        self.complete_pdf_link = page.get_by_role(
            "link",
            name="Complete PDF",
            exact=True
        )

    def open_complete_pdf(self) -> None:
        self.complete_pdf_link.click()