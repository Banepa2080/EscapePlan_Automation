import re

from playwright.sync_api import Page, expect

from pages.client.escapePlan_client_dashboard_page import ClientDashboardPage
from pages.escapePlan_login_page import LoginPage


HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_client_can_navigate_dashboard_modules(page: Page) -> None:
    login_page = LoginPage(page)
    dashboard_page = ClientDashboardPage(page)

    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie",
    )

    page.goto("https://staging-v2-dash.escapeplan.ie/login")

    login_page.login(
        "test@gmail.com",
        "test@123",
    )

    expect(page).to_have_url(
        re.compile(r".*/(?:dashboard)/?$")
    )

    # Dashboard → My Buildings
    dashboard_page.click_dashboard()
    dashboard_page.open_my_buildings()
    hold(page)

    # Open building
    dashboard_page.open_building(
        "Automated building name 20260903093936"
    )
    hold(page)

    # Building → Buildings
    dashboard_page.back_to_buildings()
    hold(page)

    # Buildings → Dashboard
    dashboard_page.click_dashboard()

    # Dashboard → Active Jobs
    dashboard_page.open_active_jobs()
    hold(page)

    # Open job
    dashboard_page.open_job(
        "Automated job title 20260903095921"
    )
    hold(page)

    # Job → Jobs
    dashboard_page.back_to_jobs()
    hold(page)

    # Jobs → Dashboard
    dashboard_page.click_dashboard()

    # Dashboard → Proposals
    dashboard_page.open_proposals()
    hold(page)

    # Open proposal
    dashboard_page.open_proposal(
        "Automated job title 20260826153305"
    )
    hold(page)

    # Proposal → Back
    dashboard_page.go_back()

    # Back → Dashboard
    dashboard_page.click_dashboard()
    hold(page)