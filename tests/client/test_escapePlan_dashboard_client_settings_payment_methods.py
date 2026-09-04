
import re
from playwright.sync_api import Page, expect

from pages.client.escapePlan_dashboard_client_settings_payment_methods_page import ClientPaymentMethodsPage
from pages.escapePlan_login_page import LoginPage


HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)



def test_client_can_update_profile(page: Page) -> None:
    login_page = LoginPage(page)
    payment_page = ClientPaymentMethodsPage(page)


 
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
        re.compile(r".*/(?:dashboard)/?$")
    )
    
    
    payment_page.add_card(
        card_number="4242 4242 4242 4242",
        expiry="04 / 26",
        cvc="147",
        zip_code="97777",
    )

    hold(page)

    payment_page.setup_stripe_payouts()