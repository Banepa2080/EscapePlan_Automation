from playwright.sync_api import Page

from pages.client.escapePlan_dashboard_client_notifications_page import (
    ClientNotificationsPage,
)
from pages.escapePlan_login_page import LoginPage


def test_client_can_open_notifications(page: Page) -> None:
    login_page = LoginPage(page)
    notifications_page = ClientNotificationsPage(page)

    # Login
    page.goto("https://staging-v2-dash.escapeplan.ie/login")

    login_page.login(
        "test@gmail.com",
        "test@123"
    )

    # Open Notifications
    notifications_page.click_notifications()