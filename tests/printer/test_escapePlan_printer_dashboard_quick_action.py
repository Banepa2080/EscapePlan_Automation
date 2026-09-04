import re
from playwright.sync_api import Page, expect
from pages.printer.escapePlan_printer_dashboard_quick_action_page import DashboardPage
from pages.printer.escapePlan_printer_login_page import LoginPage


HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_dashboard_step_wise(page: Page) -> None:
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
   

    # Step 1: Grant Chrome "Apps on device" / Local Network Access
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie"
    )

     # Step 1: Login page flow
    page.goto("https://staging-v2-dash.escapeplan.ie/login")
    # hold(page)



#method 2: using login method
    login_page.login(
            "printer@gmail.com",
            "Test@123"
        )

    expect(page).to_have_url(re.compile(r".*/dashboard/?$"))
    hold(page)


    #now open Dashboard
    dashboard_page.open_dashboard()

    # Dashboard -> Browse Available Jobs
    dashboard_page.open_view_printer_jobs()
    hold(page)
   
   
