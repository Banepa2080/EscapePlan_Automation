from playwright.sync_api import Page, expect


class ClientJobsPage:
    """Page object for navigating to and submitting the Create Job form."""

    def __init__(self, page: Page):
        self.page = page
         # Jobs navigation
        self.jobs_link = page.get_by_role("link", name="Jobs", exact=True)
        self.create_job_link = page.get_by_role("link", name="Create Job")

        # Create Job form
        self.jobs_title_input = page.get_by_role(
            "textbox", name="e.g. Fire Escape Plan"
        )
        self.building_select = page.get_by_role("combobox")
        self.jobs_drawing_size_input = page.get_by_role("textbox", name="e.g. A3")
        self.jobs_frame_colour_input = page.get_by_role("textbox", name="e.g. Black")
        self.jobs_material_input = page.get_by_role("textbox", name="e.g. Laminated")
        self.jobs_shipping_address_input = page.get_by_role(
            "textbox", name="Full shipping address"
        )
        self.jobs_notes_input = page.locator("textarea")
        self.create_job_button = page.get_by_role("button", name="Create Job")

        # Delete Job
        self.delete_button = page.get_by_role(
            "button",
            name="Delete",
            exact=True,
        )

        # # Delete confirmation dialog
        self.confirm_delete_button = page.get_by_role(
            "button",
            name="Confirm",
            exact=True,
        )   

   # Jobs Navigation Methods
    def open_create_job_form(self) -> None:
        self.jobs_link.click()
        self.create_job_link.click()

    def open_jobs(self) -> None:
        self.jobs_link.click()

    def open_latest_job(self) -> None:
        """Open the first data row from the newest-first Jobs list."""
        self.page.get_by_role("row").nth(1).get_by_role("cell").first.click()


 # Create Job Form Methods
    def enter_jobs_title(self, jobs_title: str) -> None:
        self.jobs_title_input.fill(jobs_title)

    def select_building(self, building_value: str | None = None) -> None:
        """Choose a building by value, or the first available building."""
        if building_value is not None:
            self.building_select.select_option(building_value)
        else:
            self.building_select.select_option(index=1)

    def enter_jobs_drawing_size(self, jobs_drawing_size: str) -> None:
        self.jobs_drawing_size_input.fill(jobs_drawing_size)

    def enter_frame_colour(self, frame_colour: str) -> None:
        self.jobs_frame_colour_input.fill(frame_colour)

    def enter_jobs_material(self, jobs_material: str) -> None:
        self.jobs_material_input.fill(jobs_material)

    def enter_jobs_shipping_address(self, jobs_shipping_address: str) -> None:
        self.jobs_shipping_address_input.fill(jobs_shipping_address)

    def enter_jobs_notes(self, jobs_notes: str) -> None:
        self.jobs_notes_input.fill(jobs_notes)

    def submit_create_job(self) -> None:
        self.create_job_button.click()

    def add_job(
        self,
        jobs_title: str,
        jobs_drawing_size: str,
        frame_colour: str,
        jobs_material: str,
        jobs_shipping_address: str,
        jobs_notes: str,
        building_value: str | None = None,
    ) -> None:
        """Create a new job using the supplied job details."""

        self.open_create_job_form()
        self.enter_jobs_title(jobs_title)
        self.select_building(building_value)
        self.enter_jobs_drawing_size(jobs_drawing_size)
        self.enter_frame_colour(frame_colour)
        self.enter_jobs_material(jobs_material)
        self.enter_jobs_shipping_address(jobs_shipping_address)
        self.enter_jobs_notes(jobs_notes)
        self.submit_create_job()


  # Delete Job Methods
    def open_delete_job_modal(self) -> None:
        """Open the delete confirmation modal."""
        self.delete_button.click()

    def confirm_delete_job(self) -> None:
        """Confirm job deletion from the confirmation modal."""
        self.confirm_delete_button.click()
