
# from playwright.sync_api import Page

# class HomePage:
#     def __init__(self, page:Page):
#         self.page = page
#         self.dashboard_link = page.get_by_role("link", name="Dashboard")
#         self.browse_available_jobs_link = page.get_by_role("link", name="Browse Available Jobs")
       

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

    