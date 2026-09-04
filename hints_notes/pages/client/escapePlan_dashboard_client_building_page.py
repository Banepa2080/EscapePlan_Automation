from playwright.sync_api import Page



class ClientBuildingPage:
    """Page object for navigating to and submitting the Create Building form."""

    def __init__(self, page:Page):
        self.page = page
        self.buildings_link = page.get_by_role("link", name="Buildings", exact=True)
        self.add_building_link = page.get_by_role("link", name="Add Building")
        self.building_name_input = page.get_by_role("textbox", name="e.g. Downtown Headquarters")
        self.building_address_input = page.get_by_role("textbox", name="Main St, City, State")
        self.building_details_input = page.get_by_role("textbox", name="Additional details about this")
        self.create_building_button = page.get_by_role("button", name="Create Building")
        self.edit_building_link = page.get_by_text("Edit Building", exact=True).first
        # The edit form labels are not associated with their inputs, so target
        # the form controls in their displayed order: name, address, and notes.
        self.edit_building_name_input = page.get_by_role("textbox").nth(0)
        self.edit_building_address_input = page.get_by_role("textbox").nth(1)
        self.edit_building_notes_input = page.get_by_role("textbox").nth(2)
        self.save_changes_button = page.get_by_role("button", name="Save Changes")
        self.delete_button = page.get_by_role("button", name="Delete", exact=True)
        # Once the dialog opens, its Delete confirmation is rendered after the
        # page-level Delete action.
        self.confirm_delete_button = page.get_by_role(
            "button", name="Delete", exact=True
        ).last
        self.cancel_delete_button = page.get_by_role(
            "button", name="Cancel", exact=True
        )

    def click_add_building(self):
        self.add_building_link.click()

    def open_buildings(self) -> None:
        self.buildings_link.click()

    def open_building(self, building_name: str) -> None:
        """Open a building's single-detail view from the Buildings list."""
        self.page.get_by_text(building_name, exact=False).first.click()

    def latest_building_name(self) -> str:
        """Return the name from the first data row in the newest-first list."""
        return self.page.get_by_role("row").nth(1).get_by_role("cell").first.inner_text()

    def open_latest_building(self) -> None:
        self.page.get_by_role("row").nth(1).get_by_role("cell").first.click()

    def open_edit_building_form(self) -> None:
        self.edit_building_link.click()

    def edit_building(self, building_name: str, address: str, notes: str) -> None:
        self.edit_building_name_input.fill(building_name)
        self.edit_building_address_input.fill(address)
        self.edit_building_notes_input.fill(notes)
        self.save_changes_button.click()

    def open_delete_building_modal(self) -> None:
        self.delete_button.click()

    def confirm_delete_building(self) -> None:
        self.confirm_delete_button.click()

    def cancel_delete_building(self) -> None:
        self.cancel_delete_button.click()

    def enter_building_name(self, building_name:str):
        self.building_name_input.fill(building_name)

    def enter_building_address(self, building_address:str):
        self.building_address_input.fill(building_address)

    def enter_building_details(self, building_details:str):
        self.building_details_input.fill(building_details)

    def click_create_building(self):
        self.create_building_button.click()

    def add_building(self, building_name:str, building_address:str, building_details:str):
        self.click_add_building()
        self.enter_building_name(building_name)
        self.enter_building_address(building_address)
        self.enter_building_details(building_details)
        self.click_create_building()
