
# from playwright.sync_api import Page


# class Admin_AddTemplate:

#     def __init__(self, page: Page):
#         self.page = page

#         self.add_template_link = page.get_by_role(
#             "link",
#             name="Add Template"
#         )

#     def click_add_template(self) -> None:
#         self.add_template_link.click()



from pathlib import Path

from playwright.sync_api import Page


class Admin_AddTemplate:

    def __init__(self, page: Page):
        self.page = page

        self.add_template_link = page.get_by_role(
            "link",
            name="Add Template"
        )

        self.template_name_input = page.get_by_role(
            "textbox",
            name="e.g. Fire Escape Template"
        )

        self.add_country_button = page.get_by_role(
            "button",
            name="Add Country"
        )

        self.country_input = page.get_by_role(
            "textbox",
            name="e.g. Nepal"
        )

        self.description_input = page.get_by_role(
            "textbox",
            name="Add a short description or"
        )

        self.upload_template = page.get_by_text(
            "Upload template filesDrag and"
        )

        self.create_template_button = page.get_by_role(
            "button",
            name="Create Template"
        )

    def click_add_template(self) -> None:
        self.add_template_link.click()

    def enter_template_name(self, template_name: str) -> None:
        self.template_name_input.fill(template_name)

    def click_add_country(self) -> None:
        self.add_country_button.click()

    def enter_country(self, country: str) -> None:
        self.country_input.fill(country)

    def enter_description(self, description: str) -> None:
        self.description_input.fill(description)

    def upload_template_file(self, file_path: str) -> None:
        self.page.locator(
            "input[type='file']"
        ).set_input_files(file_path)

    def click_create_template(self) -> None:
        self.create_template_button.click()