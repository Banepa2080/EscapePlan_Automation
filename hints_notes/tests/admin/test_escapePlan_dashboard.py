# import re
# from playwright.sync_api import Page, expect

# from pages.admin.escapePlan_admin_login_page import LoginPage
# # from pages.admin.escapePlan_dashboard_admin_create_users_page import UsersPage
# from pages.admin.escapePlan_admin_dashboard_page import HomePage_AddUser


# HOLD_MS = 10_000

# def hold(page: Page) -> None:
#     page.wait_for_timeout(HOLD_MS)


# # def test_admin_can_open_add_user_page(page: Page) -> None:
# #     login_page = LoginPage(page)
# #     users_page = UsersPage(page)

# #     # Open application
# #     page.goto("https://staging-v2-admin.escapeplan.ie/")

# #     # Login
# #     login_page.login("admin@escapeplan.com", "password123")

# #     # Verify login completed
# #     expect(page).not_to_have_url(
# #         "https://staging-v2-admin.escapeplan.ie/login"
# #     )

# #     # Open Add User
# #     users_page.click_add_user()

# #     # Verify Add User page opened
# #     expect(page).to_have_url(
# #         "https://staging-v2-admin.escapeplan.ie/users/add"
# #     )


# #     # Keep browser open for 10 seconds
# #     hold(page)


# def test_dashboard_step_wise(page: Page) -> None:
#     login_page = LoginPage(page)
#     home_page = HomePage_AddUser(page)

#     #     # Step 1: Grant Chrome "Apps on device" / Local Network Access
#     # page.context.grant_permissions(
#     #     ["local-network-access"],
#     #     origin="https://staging-v2-admin.escapeplan.ie"
#     # )

#      # Step 1: Login page flow
#     page.goto("https://staging-v2-admin.escapeplan.ie/login")
#     # hold(page)

#     login_page.enter_emailAddress("admin@escapeplan.com")
#     # hold(page)

#     login_page.enter_password("password123")
#     # hold(page)

#     login_page.click_login()
#     hold(page)

#     expect(page).to_have_url(re.compile(r".*/dashboard/?$"))
#     hold(page)

#     # Step 2: Dashboard page flow
#     home_page.click_dashboard()
#     # hold(page)

#     home_page.click_add_user()
#     # hold(page)
    
#     # home_page.enter_building_name("test building")
#     # # hold(page)

#     # home_page.enter_building_address("Bkt address")
#     # # hold(page)

#     # home_page.enter_building_details("test notes")
#     # # hold(page)

#     home_page.click_create_building()
#     hold(page)
