import re
from datetime import datetime

from playwright.sync_api import Page, expect

from pages.client.escapePlan_dashboard_all_clientJobs_page import ClientJobsPage
from pages.escapePlan_login_page import LoginPage
from tests.test_escapePlan_arrayUser_login import hold


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
        jobs_shipping_address="Ktm, Iran",
        jobs_notes="Automated create-job test",
    )

    # The submit action should return the user to the jobs area.
    expect(page).to_have_url(re.compile(r".*/(?:jobs|create-jobs)/?$"))
    hold(page)


def test_view_client_latest_jobs(page: Page) -> None:
    login_page = LoginPage(page)
    client_jobs_page = ClientJobsPage(page)

    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie",
    )
    page.goto("https://staging-v2-dash.escapeplan.ie/login")
    login_page.login("test@gmail.com", "test@123")

    expect(page).to_have_url(re.compile(r".*/(?:dashboard|create-jobs)/?$"))
    client_jobs_page.open_jobs()
    expect(page).to_have_url(re.compile(r".*/(?:jobs|create-jobs)/?$"))

    expect(page.get_by_role("row").nth(1)).to_be_visible()
    client_jobs_page.open_latest_job()

    # expect(page).to_have_url(re.compile(r".*/jobs/[^/]+/?$"))
    expect(page).to_have_url(
    re.compile(r".*/create-jobs/details/technician/[^/]+/?$")
    )
    hold(page)


# def test_delete_client_latest_jobs(page: Page) -> None:
#     login_page = LoginPage(page)
#     client_jobs_page = ClientJobsPage(page)

#     page.context.grant_permissions(
#         ["local-network-access"],
#         origin="https://staging-v2-dash.escapeplan.ie",
#     )
#     page.goto("https://staging-v2-dash.escapeplan.ie/login")
#     login_page.login("test@gmail.com", "test@123")

#     expect(page).to_have_url(re.compile(r".*/(?:dashboard|create-jobs)/?$"))
#     client_jobs_page.open_jobs()
#     expect(page).to_have_url(re.compile(r".*/create-jobs/?$"))

#     # job_rows = page.get_by_role("row")
#     # job_count_before_delete = job_rows.count()
#                 # OR
#     # job_count_before_delete = job_rows.count() - 1

#     # Open latest job
#     client_jobs_page.open_latest_job()
#     expect(page).to_have_url(
#     re.compile(r".*/create-jobs/details/technician/[^/]+/?$") 
# )
#     # Open delete confirmation
#     client_jobs_page.open_delete_job_modal()

#     # Confirm deletion
#     client_jobs_page.confirm_delete_job()


#     # Should return to Jobs page
#     expect(page).to_have_url(re.compile(r".*/create-jobs/?$"))

#     # One job should be removed
#     # expect(job_rows).to_have_count(job_count_before_delete - 1)
