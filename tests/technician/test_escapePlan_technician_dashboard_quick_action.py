import re
from playwright.sync_api import Page, expect
from pages.technician.escapePlan_technician_dashboard_page import AvailableJobsPage
from pages.technician.escapePlan_technician_dashboard_quick_action_page import DashboardPage
from pages.technician.escapePlan_technician_login_page import LoginPage


HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_dashboard_step_wise(page: Page) -> None:
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    available_jobs_page = AvailableJobsPage(page)


    # Step 1: Grant Chrome "Apps on device" / Local Network Access
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie"
    )

     # Step 1: Login page flow
    page.goto("https://staging-v2-dash.escapeplan.ie/login")
    # hold(page)



#method 2: using login method
    login_page.login(
            "tech@gmail.com",
            "Test@123"
        )

    expect(page).to_have_url(re.compile(r".*/dashboard/?$"))
    hold(page)

   
    # Dashboard
    dashboard_page.open_dashboard()

    # Dashboard -> Browse Available Jobs
    dashboard_page.open_browse_available_jobs()
    hold(page)

    # Open first available job
    available_jobs_page.open_first_job()
    hold(page)

    # Verify breadcrumb is displayed
    expect(page.get_by_label("Breadcrumb")).to_be_visible()

    # Job details -> Browse Jobs
    available_jobs_page.back_to_browse_jobs()
    hold(page)

    # Browse Jobs -> Dashboard
    dashboard_page.open_dashboard()

    # Verify Dashboard
    expect(
        page.get_by_role(
            "link",
            name="Dashboard",
            exact=True
        )
    ).to_be_visible()
    
    