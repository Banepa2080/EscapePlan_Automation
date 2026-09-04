from pathlib import Path

from playwright.sync_api import Page, expect

from pages.admin.escapePlan_dashboard_admin_create_symbols_page import (
    AdminCreateSymbolPage,
)
from pages.admin.escapePlan_admin_login_page import LoginPage


HOLD_MS = 10_000

def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)

def test_admin_can_create_symbol(page: Page) -> None:
    login_page = LoginPage(page)
    symbol_page = AdminCreateSymbolPage(page)

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

    #Step 3:  Open Symbols
    symbol_page.click_symbols()

    # Open Add Symbol
    symbol_page.click_add_symbol()

    # Enter symbol name
    symbol_page.enter_symbol_name("test symbol")

    # # Upload symbol file
    # file_path = (
    #     Path(__file__).parent.parent.parent
    #     / "test_data"
    #     / "tech-contracts.png"
    # )

    # symbol_page.upload_symbol_file(
    #     str(file_path)
    # )

    # Create symbol
    symbol_page.click_create_symbol()


    # Keep browser open for 10 seconds
    hold(page)
        