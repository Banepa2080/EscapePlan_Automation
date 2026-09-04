import re

from playwright.sync_api import Page, expect


class MyJobsPage:

    def __init__(self, page: Page):
        self.page = page

        self.my_jobs_link = page.get_by_role(
            "link",
            name="My Jobs",
            exact=True
        )

        self.automated_job = page.get_by_text(
            "Automated job title",
            exact=True
        )

    def open_my_jobs(self) -> None:
        self.my_jobs_link.click()

        expect(self.page).to_have_url(
            re.compile(r".*/my-jobs/?$")
        )

   

