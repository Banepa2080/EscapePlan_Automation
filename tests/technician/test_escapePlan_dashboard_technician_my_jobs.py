import re
from playwright.sync_api import Page, expect

from pages.technician.escapePlan_dashboard_technician_my_jobs_page import TechnicianMyJobsPage      
from pages.technician.escapePlan_technician_login_page import LoginPage


HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_user_can_open_and_return_from_my_job(page: Page) -> None:
    login_page = LoginPage(page)
    my_jobs_page = TechnicianMyJobsPage(page)


# Step 1: Grant Chrome "Apps on device" / Local Network Access
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie"
    )

     # Step 1: Login page flow
    page.goto("https://staging-v2-dash.escapeplan.ie/login")
    # hold(page)


    login_page.login(
            "tech@gmail.com",
            "Test@123"
        )

    expect(page).to_have_url(re.compile(r".*/dashboard/?$"))
    


    # Open My Jobs
    my_jobs_page.open_my_jobs()
    hold(page)

    # Open first job
    my_jobs_page.open_first_job()
    hold(page)

    # Verify job details page
    expect(
        page.get_by_label("Breadcrumb")
    ).to_be_visible()

    # Return to My Jobs
    my_jobs_page.back_to_my_jobs()
    hold(page)

    # Verify My Jobs page
    expect(
        page.get_by_role(
            "link",
            name="My Jobs",
            exact=True
        )
    ).to_be_visible()