from playwright.sync_api import Page


class ClientMessagesPage:
    def __init__(self, page: Page):
        self.page = page

        self.messages_link = page.get_by_role(
            "link",
            name="Messages"
        )

    def click_messages(self) -> None:
        self.messages_link.click()