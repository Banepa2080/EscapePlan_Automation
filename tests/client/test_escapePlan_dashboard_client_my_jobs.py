import re
from playwright.sync_api import Page, expect

from pages.client.escapePlan_dashboard_client_my_jobs_page import MyJobsPage
from pages.escapePlan_login_page import LoginPage

def test_user_can_view_job_proposals(page: Page) -> None:
    login_page = LoginPage(page)
    my_jobs_page = MyJobsPage(page)

    page.context.grant_permissions(
            ["local-network-access"],
            origin="https://staging-v2-dash.escapeplan.ie",
        )
    page.goto("https://staging-v2-dash.escapeplan.ie/login")
    login_page.login("test@gmail.com", "test@123")
    
    expect(page).to_have_url(re.compile(r".*/(?:dashboard|create-jobs)/?$"))
    

    # Open My Jobs
    my_jobs_page.open_my_jobs()

   