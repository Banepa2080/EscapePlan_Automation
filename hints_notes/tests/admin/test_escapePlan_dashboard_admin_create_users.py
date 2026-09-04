
import re

from playwright.sync_api import Page, expect

from pages.admin.escapePlan_dashboard_admin_create_users_page import Admin_AddUser
from pages.admin.escapePlan_admin_login_page import LoginPage


HOLD_MS = 10_000

def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)

def test_admin_can_open_add_user_page(page: Page) -> None:
    login_page = LoginPage(page)
    users_page = Admin_AddUser(page)

    # Open application
    page.goto("https://staging-v2-admin.escapeplan.ie/login")

    # Enter login details
    login_page.enter_email("admin@escapeplan.com")
    login_page.enter_password("password123")

    # print("Before click:", page.url)

    # Click Sign In
    login_page.click_sign_in()

    # Wait temporarily so we can inspect what happened
    page.wait_for_timeout(3000)

    # print("After click:", page.url)
    # print("Page text:")
    # print(page.locator("body").inner_text())


# from playwright.sync_api import Page


# def test_admin_can_open_add_user_page(page: Page) -> None:
#     login_page = LoginPage(page)

#     page.goto(
#         "https://staging-v2-admin.escapeplan.ie/login"
#     )

#     # Log API responses related to authentication
#     def log_response(response):
#         if any(word in response.url.lower() for word in ["login", "auth"]):
#             print(
#                 f"\nSTATUS: {response.status}"
#                 f"\nURL: {response.url}"
#             )

#             try:
#                 print("BODY:", response.text())
#             except Exception:
#                 pass

#     page.on("response", log_response)

#     # Login
#     login_page.enter_email("admin@escapeplan.com")
#     login_page.enter_password("password123")

#     print("\nBefore click:", page.url)

#     login_page.click_sign_in()

#     page.wait_for_timeout(3000)

#     print("\nAfter click:", page.url)


#     # Keep browser open for 10 seconds
#     hold(page)