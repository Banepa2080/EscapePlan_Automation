import re
from playwright.sync_api import Page, expect

from pages.technician.escapePlan_dashboard_technician_contracts_page import ContractsPage
from pages.client.escapePlan_client_login_page import LoginPage


HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_user_can_open_and_return_from_active_contract(
    page: Page,
) -> None:
    login_page = LoginPage(page)
    contracts_page = ContractsPage(page)

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
    

    # Open Contracts
    contracts_page.open_contracts()
    hold(page)

    # Open first ACTIVE contract
    contracts_page.open_first_active_contract()
    hold(page)

    # Verify contract details page
    expect(
        page.get_by_label("Breadcrumb")
    ).to_be_visible()

    # Return to Contracts
    contracts_page.back_to_contracts()
    hold(page)

    # Verify Contracts page
    expect(
        page.get_by_role(
            "link",
            name="Contracts",
            exact=True
        )
    ).to_be_visible()