import re
from playwright.sync_api import Page, expect
# from pages.escapePlan_login_page import LoginPage #method 2: using login method
from pages.client.escapePlan_client_login_page import LoginPage #method 1: using individual methods
from pages.client.escapePlan_client_dashboard_page import HomePage


HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_dashboard_step_wise(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)

        # Step 1: Grant Chrome "Apps on device" / Local Network Access
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie"
    )

     # Step 1: Login page flow
    page.goto("https://staging-v2-dash.escapeplan.ie/login")
    # hold(page)

# method 1: using individual methods
    login_page.enter_emailAddress("test@gmail.com")
    # hold(page)

    login_page.enter_password("test@123")
    # hold(page)

    login_page.click_login()
    hold(page)

#method 2: using login method
    # login_page.login(
    #         "test@gmail.com",
    #         "test@123"
    #     )

    expect(page).to_have_url(re.compile(r".*/dashboard/?$"))
    hold(page)

    # Step 2: Dashboard page flow
    home_page.click_dashboard()
    # hold(page)

    home_page.click_add_building()
    # hold(page)
    
    # home_page.enter_building_name("test building")
    # # hold(page)

    # home_page.enter_building_address("Bkt address")
    # # hold(page)

    # home_page.enter_building_details("test notes")
    # # hold(page)

    # home_page.click_create_building()
    hold(page)
