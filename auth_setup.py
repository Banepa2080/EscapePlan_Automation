# After creating the auth_setup.py file,this is use in conftest.py (Method 2) file to avoid login page open each time in test cases.
# then run the following command in your terminal:
# python auth_setup.py
 
# Hints: -------You should see:------
# Saved: playwright/.auth/client.json
# Saved: playwright/.auth/technician.json
# Saved: playwright/.auth/printer.json

import os
from playwright.sync_api import sync_playwright, expect


BASE_URL = "https://staging-v2-dash.escapeplan.ie"

AUTH_DIR = "playwright/.auth"


def login_and_save_state(
    browser,
    email,
    password,
    auth_file
):
    os.makedirs(AUTH_DIR, exist_ok=True)

    context = browser.new_context()

    context.grant_permissions(
        ["local-network-access"],
        origin=BASE_URL
    )

    page = context.new_page()

    page.goto(f"{BASE_URL}/login")

    page.get_by_role(
        "textbox",
        name="you@example.com"
    ).fill(email)

    page.get_by_role(
        "textbox",
        name="••••••••"
    ).fill(password)

    page.get_by_role(
        "button",
        name="Sign In"
    ).click()

    expect(page).not_to_have_url(
        f"{BASE_URL}/login"
    )

    context.storage_state(
        path=auth_file
    )

    print(f"Saved: {auth_file}")

    context.close()


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=True
    )

    # Client
    login_and_save_state(
        browser,
        "test@gmail.com",
        "test@123",
        f"{AUTH_DIR}/client.json"
    )

    # Technician
    login_and_save_state(
        browser,
        "tech@gmail.com",
        "Test@123",
        f"{AUTH_DIR}/technician.json"
    )

    # Printer
    login_and_save_state(
        browser,
        "printer1@test.com",
        "password123",
        f"{AUTH_DIR}/printer.json"
    )

    browser.close()