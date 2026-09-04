import re
from playwright.sync_api import Page, expect

from pages.printer.escapePlan_dashboard_printer_clients_page import PrinterClientsPage
from pages.printer.escapePlan_dashboard_printer_history_page import PrinterHistoryPage
from pages.technician.escapePlan_dashboard_technician_contracts_page import ContractsPage
from pages.client.escapePlan_client_login_page import LoginPage
from pages.technician.escapePlan_dashboard_technician_notifications_page import TechnicianNotificationsPage


HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_user_can_open_and_return_from_active_contract(
    page: Page,
) -> None:
    login_page = LoginPage(page)
    printer_clients_page = PrinterClientsPage(page)

    # Step 1: Grant Chrome "Apps on device" / Local Network Access
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie"
    )

     # Step 1: Login page flow
    page.goto("https://staging-v2-dash.escapeplan.ie/login")
    # hold(page)


    login_page.login(
            "printer@gmail.com",
            "Test@123"
        )

    expect(page).to_have_url(re.compile(r".*/dashboard/?$"))
    

    # Open Contracts
    printer_clients_page.open_clients()
    hold(page)

    