from playwright.sync_api import Page, expect


class AdminCreateSymbolPage:

    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.symbols_link = page.get_by_role(
            "link",
            name="Symbols"
        )

        self.add_symbol_link = page.get_by_role(
            "link",
            name="Add Symbol"
        )

        # Symbol form
        self.symbol_name_input = page.get_by_role(
            "textbox",
            name="e.g. Exit Sign"
        )

        self.file_input = page.locator(
            "input[type='file']"
        )

        self.create_symbol_button = page.get_by_role(
            "button",
            name="Create Symbol"
        )

    def click_symbols(self) -> None:
        self.symbols_link.click()

    def click_add_symbol(self) -> None:
        self.add_symbol_link.click()

    def enter_symbol_name(self, symbol_name: str) -> None:
        self.symbol_name_input.fill(symbol_name)

    def upload_symbol_file(self, file_path: str) -> None:
        self.file_input.set_input_files(file_path)

    def click_create_symbol(self) -> None:
        self.create_symbol_button.click()




# from playwright.sync_api import Page


# class AdminCreateSymbolPage:

#     def __init__(self, page: Page):
#         self.page = page

#         self.symbols_link = page.get_by_role(
#             "link",
#             name="Symbols"
#         )

#         self.add_symbol_link = page.get_by_role(
#             "link",
#             name="Add Symbol"
#         )

#         self.symbol_name_input = page.get_by_role(
#             "textbox",
#             name="e.g. Exit Sign"
#         )

#         self.upload_symbol_area = page.get_by_text(
#             "Click to upload symbol files"
#         )

#         self.create_symbol_button = page.get_by_role(
#             "button",
#             name="Create Symbol"
#         )

#     def click_symbols(self) -> None:
#         self.symbols_link.click()

#     def click_add_symbol(self) -> None:
#         self.add_symbol_link.click()

#     def enter_symbol_name(self, symbol_name: str) -> None:
#         self.symbol_name_input.fill(symbol_name)

#     def upload_symbol_file(self, file_path: str) -> None:
#         self.page.locator(
#             "input[type='file']"
#         ).set_input_files(file_path)

#     def click_create_symbol(self) -> None:
#         self.create_symbol_button.click()