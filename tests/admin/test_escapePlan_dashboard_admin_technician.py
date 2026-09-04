from playwright.sync_api import Page, expect

from pages.admin.escapePlan_admin_login_page import LoginPage
from pages.admin.escapePlan_dashboard_admin_technician_page import (
    AdminTechniciansPage,
)


HOLD_MS = 10_000

def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_admin_can_open_technician(page: Page) -> None:
    login_page = LoginPage(page)
    technicians_page = AdminTechniciansPage(page)


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




    # Open Technicians
    technicians_page.click_technicians()

    # Verify technician is displayed
    expect(
        technicians_page.technician_cell
    ).to_be_visible()

    # Open technician
    technicians_page.click_technician()


    # Keep browser open for 10 seconds
    hold(page)
            