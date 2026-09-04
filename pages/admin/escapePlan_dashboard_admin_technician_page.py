from playwright.sync_api import Page


class AdminTechniciansPage:

    def __init__(self, page: Page):
        self.page = page

        self.technicians_link = page.get_by_role(
            "link",
            name="Technicians",
            exact=True
        )

        self.technician_cell = page.get_by_role(
            "cell",
            name="Consectetur quam qu"
        )

    def click_technicians(self) -> None:
        self.technicians_link.click()

    def click_technician(self) -> None:
        self.technician_cell.click()