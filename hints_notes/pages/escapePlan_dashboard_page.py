
# from playwright.sync_api import Page

# class HomePage:
#     def __init__(self, page:Page):
#         self.page = page
#         self.dashboard_link = page.get_by_role("link", name="Dashboard")
#         self.add_building_link = page.get_by_role("link", name="Add Building")
#         self.building_name_input = page.get_by_role("textbox", name="e.g. Downtown Headquarters")
#         self.building_address_input = page.get_by_role("textbox", name="Main St, City, State")
#         self.building_details_input = page.get_by_role("textbox", name="Additional details about this")
#         self.create_building_button = page.get_by_role("button", name="Create Building")

#     def click_add_building(self):
#         self.add_building_link.click()

#     def enter_building_name(self, building_name:str):
#         self.building_name_input.fill(building_name)

#     def enter_building_address(self, building_address:str):
#         self.building_address_input.fill(building_address)

#     def enter_building_details(self, building_details:str):
#         self.building_details_input.fill(building_details)

#     def click_create_building(self):
#         self.create_building_button.click()

#     def add_building(self, building_name:str, building_address:str, building_details:str):
#         self.click_add_building()
#         self.enter_building_name(building_name)
#         self.enter_building_address(building_address)
#         self.enter_building_details(building_details)
#         self.click_create_building()

#     def click_dashboard(self):
#         self.dashboard_link.click()

    