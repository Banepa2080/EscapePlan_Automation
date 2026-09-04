from playwright.sync_api import Page


class SchedulePage:
    def __init__(self, page: Page):
        self.page = page

        self.schedule_link = page.get_by_role(
            "link",
            name="Schedule",
            exact=True
        )

    def open_schedule(self) -> None:
        self.schedule_link.click()