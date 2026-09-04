from playwright.sync_api import Page, expect

from pages.admin.escapePlan_dashboard_admin_create_admin_page import AdminCreateAdminPage

from pages.admin.escapePlan_admin_login_page import LoginPage


HOLD_MS = 10_000

def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_admin_can_create_admin(page: Page) -> None:
    login_page = LoginPage(page)
    admin_page = AdminCreateAdminPage(page)

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

    #Step 3:
    # Open Admin Users
    admin_page.click_admin_users()

    # Open Add Admin
    admin_page.click_add_admin()

    # Enter admin name
    # admin_page.enter_name("fire admin user test")
    admin_page.enter_name("Draftman admin user test")

    # Enter admin email
    # admin_page.enter_email("test11@mail.com")
    admin_page.enter_email("draftman@mail.com")

    # Select role
    admin_page.select_role("FIREMAN")
    admin_page.select_role("DRAFTSMAN")

    # Generate password
    admin_page.generate_password()

    # Enable invitation email
    admin_page.enable_invitation_email()

    # Create admin
    admin_page.click_create_admin()


    
    # Keep browser open for 10 seconds
    hold(page)
        