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

    # Step 1: Grant local network permission
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-admin.escapeplan.ie",
    )

    # Step 2: Open application
    page.goto(
        "https://staging-v2-admin.escapeplan.ie/login"
    )

    # Step 3: Login
    login_page.enter_email("admin@escapeplan.com")
    login_page.enter_password("password123")
    login_page.click_sign_in()

    # Step 4: Verify dashboard
    expect(page).to_have_url(
        "https://staging-v2-admin.escapeplan.ie/dashboard"
    )

    # Step 5: Open Symbols
    symbol_page.click_symbols()

    # Step 6: Open Add Symbol
    symbol_page.click_add_symbol()

    # Step 7: Enter Symbol Name
    symbol_page.enter_symbol_name("Automation symbol test")

    # Step 8: Upload Symbol
    file_path = (
        Path(__file__).resolve().parents[2]
        / "test_data"
        / "Capture.PNG"
    )

    assert file_path.exists(), (
        f"Symbol file not found: {file_path}"
    )

    symbol_page.upload_symbol_file(
        str(file_path)
    )

    # Step 9: Create Symbol
    symbol_page.click_create_symbol()

    # expect(page).to_have_url(
    #     "https://staging-v2-admin.escapeplan.ie/symbols"
    # )

    # Keep browser open temporarily
    hold(page)


