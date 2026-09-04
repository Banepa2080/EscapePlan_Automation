import re
from playwright.sync_api import Page, expect

from pages.printer.escapePlan_printer_dashboard_page import DashboardPage
from pages.technician.escapePlan_technician_login_page import LoginPage



HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_jobs_and_proposals_navigation(page: Page) -> None:
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
   

    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie",
    )

    page.goto("https://staging-v2-dash.escapeplan.ie/login")

    login_page.login(
        "printer@gmail.com",
        "Test@123",
    )

    expect(page).to_have_url(
        re.compile(r".*/(?:dashboard)/?$")
    )




    # Open Dashboard
    dashboard_page.go_to_dashboard()

    # Open Printer Jobs
    dashboard_page.go_to_printer_jobs()

    # Return to Dashboard
    dashboard_page.go_to_dashboard()

    # Open My Clients
    dashboard_page.go_to_my_clients()

    # Return to Dashboard
    dashboard_page.go_to_dashboard()

    # Verify we are back on Dashboard
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
