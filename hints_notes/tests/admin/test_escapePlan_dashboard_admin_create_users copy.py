
import re
from zipfile import Path

from playwright.sync_api import Page, expect

from pages.admin.escapePlan_dashboard_admin_create_templates_page import Admin_AddTemplate
from pages.admin.escapePlan_dashboard_admin_create_users_page import Admin_AddUser
from pages.admin.escapePlan_admin_login_page import LoginPage


HOLD_MS = 10_000

def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)

def test_admin_can_open_add_template_page(page: Page) -> None:
    login_page = LoginPage(page)
    users_page = Admin_AddUser(page)
    templates_page = Admin_AddTemplate(page)

    # Grant permission
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-admin.escapeplan.ie",
    )

    #Step 1: Open application
    # Open application
    page.goto("https://staging-v2-admin.escapeplan.ie/login")

    # Enter login details
    login_page.enter_email("admin@escapeplan.com")
    login_page.enter_password("password123")

   
    # Click Sign In
    login_page.click_sign_in()

    # # Wait temporarily so we can inspect what happened
    # page.wait_for_timeout(3000)

   
   #Step 2: Verify dashboard

    # Verify dashboard
    expect(page).to_have_url(
        "https://staging-v2-admin.escapeplan.ie/dashboard"
    )

#    #Step 3: Click Add User
#     # Click Add User
#     users_page.click_add_user()

#     # Verify Add User page
#     expect(page).to_have_url(
#         "https://staging-v2-admin.escapeplan.ie/users/add"
#     )

#     # Keep browser open for 10 seconds
#     hold(page)


    #Step 4 Click Add Template
    # Click Add Template
    templates_page.click_add_template()
       
     # Verify Add Template page
    expect(page).to_have_url(
        "https://staging-v2-admin.escapeplan.ie/templates/add"
    )

    # Enter template name
    templates_page.enter_template_name("test")

    # Add country
    templates_page.click_add_country()
    templates_page.enter_country("Nepal")

    # Enter description
    templates_page.enter_description("test")

    # # Upload template file
    # file_path = (
    #     Path(__file__).parent.parent.parent
    #     / "test_data"
    #     / "template.pdf"
    # )

    # templates_page.upload_template_file(
    #     str(file_path)
    # )

    # Keep browser open for 10 seconds
    hold(page)

    # Create template
    templates_page.click_create_template()
    
    # Keep browser open for 10 seconds
    hold(page)
        
    
