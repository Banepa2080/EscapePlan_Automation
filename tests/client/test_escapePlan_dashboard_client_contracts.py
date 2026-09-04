import re

from playwright.sync_api import Page, expect

from pages.escapePlan_login_page import LoginPage
from pages.client.escapePlan_dashboard_client_contracts_page import ContractsPage


def test_client_can_open_contract(page: Page) -> None:
    login_page = LoginPage(page)
    contracts_page = ContractsPage(page)

    # Login
    page.goto("https://staging-v2-dash.escapeplan.ie/login")

    login_page.login(
        "test@gmail.com",
        "test@123"
    )

    # Verify login
    expect(page).to_have_url(
        re.compile(r".*/(?:dashboard|create-jobs)/?$")
    )

    # Open Contracts
    contracts_page.open_contracts()

    # Verify Technician is displayed
    contracts_page.verify_technician_visible()

    # Open Bkt contract
    contracts_page.open_bkt_contract()