
# # Important notes about why to use conftest.py in pytest:
# # Without conftest.py, you'd need to write this same code in every test file:
# # That’s repeating code and not good practice. 😖
# # With conftest.py  we define that once as a fixture and just use it in tests
# # A fixture is a reusable piece of code that sets something up before a test runs, and can clean it up afterward


#for youtube video reference: https://www.youtube.com/watch?v=VZ5LU8vHT0s&list=PLhW3qG5bs-L8WcAa9cfXaqGe0-Cq85y4X
# import pytest
# from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="session")
# def  browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)  # set headless=True if you don't want to see the browser window
#         yield browser
#         browser.close()

# @pytest.fixture
# def page(browser):
#     page = browser.new_page()
#     yield page
#     page.close()

# Live project of Office:
#-----EscapePlan----> for user login one time and then use the same session for all tests, we can use a fixture to log in once and store the session state in a file. Then, we can load that session state in subsequent tests to avoid logging in again.
import os
import pytest
from playwright.sync_api import Page, expect

#------------------For printer login and then open messages page---------------
BASE_URL = "https://staging-v2-dash.escapeplan.ie"
AUTH_FILE = "playwright/.auth/printer.json"


@pytest.fixture(scope="session")
def printer_auth_state(browser):
    """Login once and save Printer authentication state."""

    os.makedirs("playwright/.auth", exist_ok=True)

    context = browser.new_context()
    page = context.new_page()

    page.goto(f"{BASE_URL}/login")

    

    page.get_by_role(
        "textbox",
        name="you@example.com"
    ).fill("printer1@test.com")

    page.get_by_role(
        "textbox",
        name="••••••••"
    ).fill("password123")

    page.get_by_role(
        "button",
        name="Sign In"
    ).click()

    # Wait until login is completed
    expect(page).not_to_have_url(
        f"{BASE_URL}/login"
    )

    

    # Save authentication
    context.storage_state(path=AUTH_FILE)

    context.close()

    return AUTH_FILE


@pytest.fixture
def printer_page(browser, printer_auth_state):
    """Create an authenticated Printer page."""

    context = browser.new_context(
        storage_state=printer_auth_state
    )

    page = context.new_page()

    # Grant Chrome local network access
    page.context.grant_permissions(
        ["local-network-access"],
        origin=BASE_URL
    )

    # IMPORTANT:
    # New page starts at about:blank.
    # Navigate to the application / Open application
    page.goto(BASE_URL)

    # Optional verification
    # expect(page).not_to_have_url(
    #     f"{BASE_URL}/login"
    # )

    yield page

    context.close()