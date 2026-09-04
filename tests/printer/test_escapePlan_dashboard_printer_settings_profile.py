
import re
from playwright.sync_api import Page, expect


from pages.escapePlan_login_page import LoginPage
from pages.printer.escapePlan_dashboard_printer_settings_profile_page import PrinterProfileSettingsPage


HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)



def test_client_can_update_profile(page: Page) -> None:
    login_page = LoginPage(page)
    profile_settings_page = PrinterProfileSettingsPage(page)

 
    # Browser permission
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie",
    )

    
    # Login
    page.goto(
        "https://staging-v2-dash.escapeplan.ie/login"
    )

    login_page.login(
        "printer@gmail.com",
        "Test@123",
    )

    # Verify successful login
    expect(page).to_have_url(
        re.compile(r".*/(?:dashboard|create-jobs)/?$")
    )
    
    
    profile_settings_page.update_profile(
        full_name="ktm",
        phone="1478529630",
        company="team kavre",
        address="ktm",
        city="ktm",
        postcode="12345",
        country="Nepal",
    )