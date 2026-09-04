from playwright.sync_api import Page , expect

from pages.admin.escapePlan_dashboard_admin_create_price_page import (
    AdminCreatePricingPage,
)
from pages.admin.escapePlan_admin_login_page import LoginPage


HOLD_MS = 10_000

def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_admin_can_create_pricing_plan(page: Page) -> None:
    login_page = LoginPage(page)
    pricing_page = AdminCreatePricingPage(page)

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
    # Open Pricing
    pricing_page.click_pricing()

    # Open Add Plan
    pricing_page.click_add_plan()

    # Enter plan name
    pricing_page.enter_plan_name("basic plan")

    # Enter price
    pricing_page.enter_price("20")

    # # Select currency
    # pricing_page.select_currency("USD")

    # # Select plan type
    # pricing_page.select_plan_type("RECURRING")

    # Create plan
    pricing_page.click_create_plan()

    # Step 4: Verify plan was created
    # expect(page.get_by_text("basic plan", exact=True)).to_be_visible()
    expect(page).to_have_url(
        "https://staging-v2-admin.escapeplan.ie/admin-pricing"
    )

    # Keep browser open for 10 seconds
    hold(page)
        