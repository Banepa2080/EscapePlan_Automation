import re
from playwright.sync_api import Page, expect

from pages.admin.escapePlan_admin_dashboard_page import AdminDashboardPage
from pages.admin.escapePlan_admin_login_page import LoginPage
# from pages.admin.escapePlan_dashboard_admin_create_users_page import UsersPage
from pages.admin.escapePlan_admin_dashboard_add_page import Admin_AddUser,Admin_AddTemplate,Admin_AddSymbol,Admin_AddPricing


HOLD_MS = 5_000

def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


# def test_admin_can_open_add_user_page(page: Page) -> None:
#     login_page = LoginPage(page)
#     users_page = UsersPage(page)

#     # Open application
#     page.goto("https://staging-v2-admin.escapeplan.ie/")

#     # Login
#     login_page.login("admin@escapeplan.com", "password123")

#     # Verify login completed
#     expect(page).not_to_have_url(
#         "https://staging-v2-admin.escapeplan.ie/login"
#     )

#     # Open Add User
#     users_page.click_add_user()

#     # Verify Add User page opened
#     expect(page).to_have_url(
#         "https://staging-v2-admin.escapeplan.ie/users/add"
#     )


#     # Keep browser open for 10 seconds
#     hold(page)


def test_dashboard_step_wise(page: Page) -> None:
    login_page = LoginPage(page)
    dashboard = AdminDashboardPage(page)
    home_add_user_page = Admin_AddUser(page)
    home_add_template_page = Admin_AddTemplate(page)
    home_add_symbol_page = Admin_AddSymbol(page)
    home_add_pricing_page = Admin_AddPricing(page)

    # Step 1: Grant Chrome "Apps on device" / Local Network Access
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-admin.escapeplan.ie"
    )

     # Step 1: Login page flow
    page.goto("https://staging-v2-admin.escapeplan.ie/login")
    

    login_page.enter_email("admin@escapeplan.com")
   

    login_page.enter_password("password123")
    

    # Click Sign In
    login_page.click_sign_in()
    hold(page)

    #Step 2: Verify dashboard
    # Verify dashboard
    expect(page).to_have_url(
        "https://staging-v2-admin.escapeplan.ie/dashboard"
    )
  

    # # # Step 2: Dashboard page flow
    home_add_user_page.click_add_user()
    hold(page)

    dashboard.click_dashboard()
    home_add_template_page.click_add_template()
    hold(page)

    dashboard.click_dashboard()
    home_add_symbol_page.click_add_symbol()
    hold(page)

    dashboard.click_dashboard()
    home_add_pricing_page.click_add_pricing()
    hold(page)





# import re

# from playwright.sync_api import Page, expect

# from pages.admin.escapePlan_dashboard_admin_create_users_page import Admin_AddUser
# from pages.admin.escapePlan_admin_login_page import LoginPage


# HOLD_MS = 10_000

# def hold(page: Page) -> None:
#     page.wait_for_timeout(HOLD_MS)

# def test_admin_can_open_add_user_page(page: Page) -> None:
#     login_page = LoginPage(page)
#     users_page = Admin_AddUser(page)

#     # Grant permission
#     page.context.grant_permissions(
#         ["local-network-access"],
#         origin="https://staging-v2-admin.escapeplan.ie",
#     )


#     # Open application
#     page.goto("https://staging-v2-admin.escapeplan.ie/login")

#     # Enter login details
#     login_page.enter_email("admin@escapeplan.com")
#     login_page.enter_password("password123")

#     # print("Before click:", page.url)

#     # Click Sign In
#     login_page.click_sign_in()

#     # Wait temporarily so we can inspect what happened
#     page.wait_for_timeout(3000)

#     # print("After click:", page.url)
#     # print("Page text:")
#     # print(page.locator("body").inner_text())
    
    
#     # Keep browser open for 10 seconds
#     hold(page)


# # from playwright.sync_api import Page


# # def test_admin_can_open_add_user_page(page: Page) -> None:
# #     login_page = LoginPage(page)

# #     page.goto(
# #         "https://staging-v2-admin.escapeplan.ie/login"
# #     )

# #     # Log API responses related to authentication
# #     def log_response(response):
# #         if any(word in response.url.lower() for word in ["login", "auth"]):
# #             print(
# #                 f"\nSTATUS: {response.status}"
# #                 f"\nURL: {response.url}"
# #             )

# #             try:
# #                 print("BODY:", response.text())
# #             except Exception:
# #                 pass

# #     page.on("response", log_response)

# #     # Login
# #     login_page.enter_email("admin@escapeplan.com")
# #     login_page.enter_password("password123")

# #     print("\nBefore click:", page.url)

# #     login_page.click_sign_in()

# #     page.wait_for_timeout(3000)

# #     print("\nAfter click:", page.url)


# #     # Keep browser open for 10 seconds
# #     hold(page)
