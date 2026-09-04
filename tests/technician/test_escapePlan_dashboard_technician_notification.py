from playwright.sync_api import Page


from pages.escapePlan_login_page import LoginPage
from pages.technician.escapePlan_dashboard_technician_notifications_page import TechnicianNotificationsPage


def test_client_can_open_notifications(page: Page) -> None:
    login_page = LoginPage(page)
    notifications_page = TechnicianNotificationsPage(page)

    # Login
    page.goto("https://staging-v2-dash.escapeplan.ie/login")

    login_page.login(
        "tech@gmail.com",
        "Test@123"
    )

    # Open Notifications
    notifications_page.click_notifications()