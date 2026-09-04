# # method 1 :- without auth_setup.py file

import os
import pytest
from playwright.sync_api import expect


BASE_URL = "https://staging-v2-dash.escapeplan.ie"

# PRINTER_AUTH = "playwright/.auth/printer.json"
# TECHNICIAN_AUTH = "playwright/.auth/technician.json"
# CLIENT_AUTH = "playwright/.auth/client.json"

AUTH_DIR = "playwright/.auth"

PRINTER_AUTH = f"{AUTH_DIR}/printer.json"
TECHNICIAN_AUTH = f"{AUTH_DIR}/technician.json"
CLIENT_AUTH = f"{AUTH_DIR}/client.json"



# ============================================================
# Helper function: LOGIN + SAVE AUTH
# ============================================================

def login_and_save_state(browser, email, password, auth_file):
    """
    Login once and save the authenticated browser state.
    """

    # os.makedirs("playwright/.auth", exist_ok=True)
    os.makedirs(AUTH_DIR, exist_ok=True)

    context = browser.new_context()
    page = context.new_page()

    # Grant local network access
    page.context.grant_permissions(
        ["local-network-access"],
        origin=BASE_URL
    )

    # Open login page
    page.goto(f"{BASE_URL}/login")

    # Enter credentials
    page.get_by_role(
        "textbox",
        name="you@example.com"
    ).fill(email)

    page.get_by_role(
        "textbox",
        name="••••••••"
    ).fill(password)

    # Login
    page.get_by_role(
        "button",
        name="Sign In"
    ).click()

    # Verify login succeeded
    expect(page).not_to_have_url(
        f"{BASE_URL}/login"
    )

    # Save cookies/local storage
    context.storage_state(path=auth_file)
    
    print(f"\nSaved auth state: {auth_file}")

    context.close()

    return auth_file


# ============================================================
# PRINTER AUTH
# ============================================================

@pytest.fixture(scope="session")
def printer_auth_state(browser):

    return login_and_save_state(
        browser,
        "printer@test.com",
        "Test@1234",
        # "printer1@test.com",
        # "password123",
        PRINTER_AUTH
    )



# ============================================================
# PRINTER PAGE
# ============================================================

@pytest.fixture
def printer_page(browser, printer_auth_state):

    context = browser.new_context(
        storage_state=printer_auth_state
    )

    # Grant permission to this new context
    context.grant_permissions(
        ["local-network-access"],
        origin=BASE_URL
    )

    page = context.new_page()

    # Open application
    page.goto(BASE_URL)

    expect(page).not_to_have_url(
        f"{BASE_URL}/login"
    )

    yield page

    context.close()


# ============================================================
# TECHNICIAN AUTH
# ============================================================

@pytest.fixture(scope="session")
def technician_auth_state(browser):
    return login_and_save_state(
        browser,
        # "technician1@test.com",
        # "password123",
        "tech@gmail.com",
        "Test@123",
        TECHNICIAN_AUTH
    )


# ============================================================
# TECHNICIAN PAGE
# ============================================================

@pytest.fixture
def technician_page(browser, technician_auth_state):

    context = browser.new_context(
        storage_state=technician_auth_state
    )

    # Grant local network access
    context.grant_permissions(
        ["local-network-access"],
        origin=BASE_URL
    )

    page = context.new_page()

    # Open application
    page.goto(BASE_URL)

    expect(page).not_to_have_url(
        f"{BASE_URL}/login"
    )

    yield page

    context.close()


# ============================================================
# CLIENT AUTH
# ============================================================

@pytest.fixture(scope="session")
def client_auth_state(browser):
    return login_and_save_state(
        browser,
        # "client1@test.com",
        # "password123",
        "test@gmail.com",
        "test@123",
        CLIENT_AUTH
    )

# ============================================================
# CLIENT PAGE
# ============================================================

@pytest.fixture
def client_page(browser, client_auth_state):

    context = browser.new_context(
        storage_state=client_auth_state
    )

    # Grant local network access
    context.grant_permissions(
        ["local-network-access"],
        origin=BASE_URL
    )

    page = context.new_page()

    # Open application
    page.goto(BASE_URL)

    # expect(page).not_to_have_url(
    #     f"{BASE_URL}/login"
    # )
    page.goto(f"{BASE_URL}/dashboard")

    yield page

    context.close()





# #method 2 :- with auth_setup.py file (without login page open each time)
# import os
# import pytest
# from playwright.sync_api import expect


# BASE_URL = "https://staging-v2-dash.escapeplan.ie"

# CLIENT_AUTH = "playwright/.auth/client.json"
# TECHNICIAN_AUTH = "playwright/.auth/technician.json"
# PRINTER_AUTH = "playwright/.auth/printer.json"


# @pytest.fixture
# def client_page(browser):

#     context = browser.new_context(
#         storage_state=CLIENT_AUTH
#     )

#     context.grant_permissions(
#         ["local-network-access"],
#         origin=BASE_URL
#     )

#     page = context.new_page()

#     page.goto(BASE_URL)

#     expect(page).not_to_have_url(
#         f"{BASE_URL}/login"
#     )

#     yield page

#     context.close()


# @pytest.fixture
# def technician_page(browser):

#     context = browser.new_context(
#         storage_state=TECHNICIAN_AUTH
#     )

#     context.grant_permissions(
#         ["local-network-access"],
#         origin=BASE_URL
#     )

#     page = context.new_page()

#     page.goto(BASE_URL)

#     expect(page).not_to_have_url(
#         f"{BASE_URL}/login"
#     )

#     yield page

#     context.close()


# @pytest.fixture
# def printer_page(browser):

#     context = browser.new_context(
#         storage_state=PRINTER_AUTH
#     )

#     context.grant_permissions(
#         ["local-network-access"],
#         origin=BASE_URL
#     )

#     page = context.new_page()

#     page.goto(BASE_URL)

#     expect(page).not_to_have_url(
#         f"{BASE_URL}/login"
#     )

#     yield page

#     context.close()