#one time login required for each test case, after that no need to login again for other test cases

from playwright.sync_api import Page

from conftest import technician_page
from pages.technician.escapePlan_dashboard_technician_messages_page import (TechnicianMessagesPage)



HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_client_can_open_messages(technician_page: Page) -> None:
    messages_page = TechnicianMessagesPage(technician_page)

    # Open Messages
    messages_page.click_messages()
    hold(technician_page)



# each time login required 
# from playwright.sync_api import Page


# from pages.escapePlan_login_page import LoginPage
# from pages.technician.escapePlan_dashboard_technician_messages_page import TechnicianMessagesPage


# def test_client_can_open_messages(page: Page) -> None:
#     login_page = LoginPage(page)
#     messages_page = TechnicianMessagesPage(page)

#     # Login
#     page.goto("https://staging-v2-dash.escapeplan.ie/login")

#     login_page.login(
#         "tech@gmail.com",
#         "Test@123"
#     )

#     # Open Messages
#     messages_page.click_messages()