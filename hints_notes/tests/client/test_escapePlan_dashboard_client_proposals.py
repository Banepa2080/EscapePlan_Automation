
import re

from playwright.sync_api import Page, expect

from pages.client.escapePlan_dashboard_client_proposals_page import (
    ClientProposalsPage,
)
from pages.escapePlan_login_page import LoginPage


HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_accept_client_latest_proposal(page: Page) -> None:
    login_page = LoginPage(page)
    client_proposals_page = ClientProposalsPage(page)

    
    # Browser permission
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie",
    )

    
    # Login
    page.goto(
        "https://staging-v2-dash.escapeplan.ie/login"
    )

    login_page.login(
        "test@gmail.com",
        "test@123",
    )

    # Verify successful login
    expect(page).to_have_url(
        re.compile(r".*/(?:dashboard|create-jobs)/?$")
    )
    
    # Step 1: Open Proposals
    client_proposals_page.open_proposals()

    expect(page).to_have_url(
        re.compile(r".*/proposals/?$")
    )

    
    # Step 2: Open Job proposals
    client_proposals_page.open_job_2_proposals()

    # Verify proposals are available
    expect(
        page.get_by_text(
            re.compile(r"\d+\s+proposal\(s\)", re.I)
        )
    ).to_be_visible()

    
    # Step 3: Open latest proposal
    client_proposals_page.open_latest_proposal()

    # Expected:
    # /proposals/{proposal_id}
    expect(page).to_have_url(
        re.compile(
            r".*/proposals/[^/]+/?$"
        )
    )

    
    # Step 4: Open final proposal details
    client_proposals_page.open_final_proposal()

    # Expected:
    # /proposals/{proposal_id}/{proposal_detail_id}
    expect(page).to_have_url(
        re.compile(
            r".*/proposals/[^/]+/[^/]+/?$"
        )
    )

    
    # Step 5: Verify Accept Proposal button
    expect(
        client_proposals_page.accept_proposal_button
    ).to_be_visible()

    
    # Step 6: Accept proposal
    client_proposals_page.click_accept_proposal()

    hold(page)