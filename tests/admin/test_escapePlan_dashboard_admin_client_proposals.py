from playwright.sync_api import Page, expect

from pages.admin.escapePlan_admin_login_page import LoginPage
from pages.admin.escapePlan_dashboard_admin_client_proposals_page import (
    AdminProposalsPage,
)



HOLD_MS = 5_000

def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)



def test_admin_can_open_proposal_and_return(page: Page) -> None:
    login_page = LoginPage(page)
    proposals_page = AdminProposalsPage(page)

 # Step 1: Grant Chrome "Apps on device" / Local Network Access
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-admin.escapeplan.ie"
    )

     # Step 1: Login page flow
    page.goto("https://staging-v2-admin.escapeplan.ie/login")
    

    login_page.enter_email("admin@escapeplan.com")
   

    login_page.enter_password("password123")
    

    # Click Sign In
    login_page.click_sign_in()
    hold(page)

    #Step 2: Verify dashboard
    # Verify dashboard
    expect(page).to_have_url(
        "https://staging-v2-admin.escapeplan.ie/dashboard"
    )
  

    # Open Proposals
    proposals_page.click_proposals()

    # Open Automated job title proposal
    proposals_page.open_proposal("Automated job title")

    # Return to Proposals
    proposals_page.back_to_proposals()