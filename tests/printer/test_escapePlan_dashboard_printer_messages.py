# from playwright.sync_api import Page


# from pages.escapePlan_login_page import LoginPage
# from pages.printer.escapePlan_dashboard_printer_messages_page import PrinterMessagesPage
# from pages.technician.escapePlan_dashboard_technician_messages_page import TechnicianMessagesPage

# HOLD_MS = 10_000


# def hold(page: Page) -> None:
#     page.wait_for_timeout(HOLD_MS)

# def test_client_can_open_messages(page: Page) -> None:
#     login_page = LoginPage(page)
#     messages_page = PrinterMessagesPage(page)

#     # Login
#     page.goto("https://staging-v2-dash.escapeplan.ie/login")

#     login_page.login(
#         # "printer@gmail.com",
#         # "Test@123"
#         "printer1@test.com",
#         "password123"
#     )

#     # Open Messages
#     messages_page.click_messages()
#     hold(page)



#-----Save login session and use it for all tests, so that we don't have to login again and again for each test case. We can use a fixture to log in once and store the session state in a file. Then, we can load that session state in subsequent tests to avoid logging in again.
#using fixture(conftest.py) for printer login and then open messages page
from playwright.sync_api import Page

from conftest import printer_page
from pages.printer.escapePlan_dashboard_printer_messages_page import (
    PrinterMessagesPage
)


HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_printer_can_open_messages(printer_page: Page) -> None:

    messages_page = PrinterMessagesPage(printer_page)
    # hold(printer_page)

    messages_page.click_messages()
    hold(printer_page)