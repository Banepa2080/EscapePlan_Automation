import re
from playwright.sync_api import Page, expect

from pages.technician.escapePlan_technician_dashboard_page import DashboardPage,AvailableJobsPage,ActiveJobsPage,ProposalsPage
from pages.technician.escapePlan_technician_login_page import LoginPage



HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_jobs_and_proposals_navigation(page: Page) -> None:
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    available_jobs_page = AvailableJobsPage(page)
    active_jobs_page = ActiveJobsPage(page)
    proposals_page = ProposalsPage(page)


    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie",
    )

    page.goto("https://staging-v2-dash.escapeplan.ie/login")

    login_page.login(
        "tech@gmail.com",
        "Test@123",
    )

    expect(page).to_have_url(
        re.compile(r".*/(?:dashboard)/?$")
    )



    
    # 1. Dashboard -> Available Jobs
    dashboard_page.open_dashboard()
    dashboard_page.open_available_jobs()
    hold(page)

    # 2. Open first Available Job
    available_jobs_page.open_first_job()
    expect(page.get_by_label("Breadcrumb")).to_be_visible()
    hold(page)

    # 3. Available Job -> Browse Jobs
    available_jobs_page.back_to_browse_jobs()
    hold(page)

    # 4. Dashboard -> Active Jobs
    dashboard_page.open_dashboard()
    dashboard_page.open_active_jobs()
    hold(page)

    # 5. Open first Active Job
    active_jobs_page.open_first_active_job()
    expect(page.get_by_label("Breadcrumb")).to_be_visible()
    hold(page)

    # 6. Active Job -> My Jobs
    active_jobs_page.back_to_my_jobs()
    hold(page)

    # 7. Dashboard -> Proposals Sent
    dashboard_page.open_dashboard()
    dashboard_page.open_proposals_sent()
    hold(page)

    # 8. Open first Proposal
    proposals_page.open_first_proposal()
    expect(page.get_by_label("Breadcrumb")).to_be_visible()
    hold(page)

    # 9. Proposal -> My Proposals
    proposals_page.back_to_my_proposals()
    hold(page)

    # 10. Return to Dashboard
    dashboard_page.open_dashboard()
    expect(page.get_by_role(
        "link",
        name="Dashboard",
        exact=True
    )).to_be_visible()