from playwright.sync_api import Page


class TechnicianNotificationsPage:
    def __init__(self, page: Page):
        self.page = page

        self.notifications_link = page.get_by_role(
            "link",
            name="Notifications"
        )

    def click_notifications(self) -> None:
        self.notifications_link.click()