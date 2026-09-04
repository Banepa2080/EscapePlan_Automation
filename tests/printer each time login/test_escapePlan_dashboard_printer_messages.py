from playwright.sync_api import Page


from pages.escapePlan_login_page import LoginPage
from pages.printer.escapePlan_dashboard_printer_messages_page import PrinterMessagesPage
from pages.technician.escapePlan_dashboard_technician_messages_page import TechnicianMessagesPage

HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)

def test_client_can_open_messages(page: Page) -> None:
    login_page = LoginPage(page)
    messages_page = PrinterMessagesPage(page)

    # Login
    page.goto("https://staging-v2-dash.escapeplan.ie/login")

    login_page.login(
        # "printer@gmail.com",
        # "Test@123"
        "printer1@test.com",
        "password123"
    )

    # Open Messages
    messages_page.click_messages()
    hold(page)