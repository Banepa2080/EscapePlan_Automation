# Method 1 :- without auth_setup.py file OR playwright/.auth/..... file

from playwright.sync_api import Page

from pages.client.escapePlan_dashboard_client_messages_page import (
    ClientMessagesPage,
)

HOLD_MS = 10_000

def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_client_can_open_messages(client_page: Page) -> None:
    messages_page = ClientMessagesPage(client_page)
    hold(client_page)

    # Open Messages
    messages_page.click_messages()
    hold(client_page)



# each time login required 

# from playwright.sync_api import Page

# from pages.client.escapePlan_dashboard_client_messages_page import (
#     ClientMessagesPage,
# )
# from pages.escapePlan_login_page import LoginPage


# def test_client_can_open_messages(page: Page) -> None:
#     login_page = LoginPage(page)
#     messages_page = ClientMessagesPage(page)

#     # Login
#     page.goto("https://staging-v2-dash.escapeplan.ie/login")

#     login_page.login(
#         "test@gmail.com",
#         "test@123"
#     )

#     # Open Messages
#     messages_page.click_messages()


