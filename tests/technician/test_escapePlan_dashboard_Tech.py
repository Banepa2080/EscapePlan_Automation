import re
from datetime import date, timedelta

import pytest
from playwright.sync_api import Page, expect

from pages.technician.escapePlan_dashboard_tech_browseJobs_page import TechnicianBrowseJobsPage
from pages.escapePlan_login_page import LoginPage


def test_technician_can_submit_proposal(page: Page) -> None:
    login_page = LoginPage(page)
    browse_jobs_page = TechnicianBrowseJobsPage(page)

    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie",
    )
    page.goto("https://staging-v2-dash.escapeplan.ie/login")
    login_page.login("tech@gmail.com", "Test@123")

    expect(page).to_have_url(re.compile(r".*/(?:dashboard|browse-jobs)/?$"))

    browse_jobs_page.open_browse_jobs()
    if not browse_jobs_page.has_available_jobs():
        pytest.skip("No jobs are currently available for technician proposals.")

    start_date = date.today()
    end_date = start_date + timedelta(days=2)
    browse_jobs_page.submit_job_proposal(
        expertise="Fire Safety Expert",
        estimated_days="5",
        proposed_cost="500",
        start_date=start_date.isoformat(),
        end_date=end_date.isoformat(),
        approach="Detailed fire-safety assessment and escape-plan proposal.",
        risks="Access limitations and incomplete building information.",
        design_strategy="Use the supplied building information and safety standards.",
        notes="Automated proposal submission test.",
    )

    expect(page.get_by_text("5", exact=True).first).to_be_visible()
