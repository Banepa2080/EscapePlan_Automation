import re
from playwright.sync_api import Page, expect

from pages.technician.escapePlan_dashboard_technician_my_proposals_page import TechnicianMyProposalsPage    
from pages.technician.escapePlan_technician_login_page import LoginPage


HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)



def test_user_can_open_and_return_from_my_proposal(
    page: Page,
) -> None:
    login_page = LoginPage(page)
    my_proposals_page = TechnicianMyProposalsPage(page)

    # Step 1: Grant Chrome "Apps on device" / Local Network Access
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie"
    )

     # Step 1: Login page flow
    page.goto("https://staging-v2-dash.escapeplan.ie/login")
    # hold(page)

    # login
    login_page.login(
            "tech@gmail.com",
            "Test@123"
        )

    expect(page).to_have_url(re.compile(r".*/dashboard/?$"))



    # Open My Proposals
    my_proposals_page.open_my_proposals()
    hold(page)

    # Open first proposal
    my_proposals_page.open_first_proposal()
    hold(page)

    # Verify proposal details page
    expect(
        page.get_by_label("Breadcrumb")
    ).to_be_visible()

    # Return to My Proposals
    my_proposals_page.back_to_my_proposals()
    hold(page)
    
    # Verify My Proposals page
    expect(
        page.get_by_role(
            "link",
            name="My Proposals",
            exact=True
        )
    ).to_be_visible()