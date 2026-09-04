
from playwright.sync_api import Page

class HomePage_AddUser:
    def __init__(self, page:Page):
        self.page = page
        self.dashboard_link = page.get_by_role("link", name="Dashboard")
        self.add_user_link = page.get_by_role("link", name="Add User")
        # self.building_name_input = page.get_by_role("textbox", name="e.g. Downtown Headquarters")
        # self.building_address_input = page.get_by_role("textbox", name="Main St, City, State")
        # self.building_details_input = page.get_by_role("textbox", name="Additional details about this")
        # self.create_building_button = page.get_by_role("button", name="Create Building")

    def click_add_user(self):
        self.add_user_link.click()
        
    def open_dashboard(self) -> None:
        self.dashboard_link.click()

   


    # def enter_building_name(self, building_name:str):
    #     self.building_name_input.fill(building_name)

    # def enter_building_address(self, building_address:str):
    #     self.building_address_input.fill(building_address)

    # def enter_building_details(self, building_details:str):
    #     self.building_details_input.fill(building_details)

    # def click_create_building(self):
    #     self.create_building_button.click()

    def add_users(self, user_name:str, user_address:str, user_details:str):
        self.click_add_user()
        # self.enter_user_name(user_name)
        # self.enter_user_address(user_address)
        # self.enter_user_details(user_details)
        # self.click_create_user()

    # def click_dashboard(self):
    #     self.dashboard_link.click()

    