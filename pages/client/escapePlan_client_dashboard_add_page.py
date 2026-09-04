from playwright.sync_api import Page


class Client_AddBuilding:

    def __init__(self, page: Page):
        self.page = page

        self.add_building_link = page.get_by_role(
            "link",
            name="Add Building"
        )

    def click_add_building(self) -> None:
        self.add_building_link.click()



class Client_CreateTechnicianJob:

    def __init__(self, page: Page):
        self.page = page

        self.create_technician_job_link = page.get_by_role(
            "link",
            name=" Create Technician Job"
        )

    def click_create_technician_job(self) -> None:
        self.create_technician_job_link.click()

class Client_CreatePrinterJob:

    def __init__(self, page: Page):
        self.page = page

        self.create_printer_job_link = page.get_by_role(
            "link",
            name=" Create Printer Job"
        )

    def click_create_printer_job(self) -> None:
        self.create_printer_job_link.click()
