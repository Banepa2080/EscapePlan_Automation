from playwright.sync_api import Page


from pages.escapePlan_login_page import LoginPage
from pages.printer.escapePlan_dashboard_printer_notifications_page import PrinterNotificationsPage

HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_client_can_open_notifications(page: Page) -> None:
    login_page = LoginPage(page)
    notifications_page = PrinterNotificationsPage(page)

    # Login
    page.goto("https://staging-v2-dash.escapeplan.ie/login")

    login_page.login(
        # "printer@gmail.com",
        # "Test@123"
        "printer1@test.com",
        "password123"
    )

    # Open Notifications
    notifications_page.click_notifications()
    hold(page)