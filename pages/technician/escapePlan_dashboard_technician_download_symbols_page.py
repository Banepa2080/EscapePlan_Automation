from playwright.sync_api import Page


class DownloadsPage:
    def __init__(self, page: Page):
        self.page = page

        self.downloads_link = page.get_by_role(
            "link",
            name="Downloads",
            exact=True
        )

    def open_downloads(self) -> None:
        self.downloads_link.click()