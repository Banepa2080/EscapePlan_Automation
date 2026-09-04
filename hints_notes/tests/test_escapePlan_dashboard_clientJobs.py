import re
from datetime import datetime

from playwright.sync_api import Page, expect

from pages.client.escapePlan_dashboard_clientJobs_page import ClientJobsPage
from pages.escapePlan_login_page import LoginPage


def test_create_client_job(page: Page) -> None:
    login_page = LoginPage(page)
    client_jobs_page = ClientJobsPage(page)

    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie",
    )
    page.goto("https://staging-v2-dash.escapeplan.ie/login")
    login_page.login("test@gmail.com", "test@123")

    expect(page).to_have_url(re.compile(r".*/(?:dashboard|create-jobs)/?$"))

    # A unique name keeps repeated test executions from creating ambiguous records.
    job_title = f"Automated job title {datetime.now():%Y%m%d%H%M%S}"
    client_jobs_page.add_job(
        jobs_title=job_title,
        jobs_drawing_size="A4",
        frame_colour="Black and white",
        jobs_material="Laminated",
        jobs_shipping_address="Ktm, iseland, notestt",
        jobs_notes="Automated create-job test",
    )

    # The submit action should return the user to the jobs area.
    expect(page).to_have_url(re.compile(r".*/(?:jobs|create-jobs)/?$"))
