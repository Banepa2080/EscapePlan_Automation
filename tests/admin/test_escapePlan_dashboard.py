from playwright.sync_api import Page, expect

from pages.admin.escapePlan_admin_dashboard_page import AdminDashboardPage
from pages.admin.escapePlan_admin_login_page import LoginPage


HOLD_MS = 10_000

def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)

def test_admin_can_navigate_dashboard_modules(page: Page) -> None:
    login_page = LoginPage(page)
    dashboard = AdminDashboardPage(page)

 # Grant permission
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-admin.escapeplan.ie",
    )

    #Step 1: Open application
    # Open application
    page.goto("https://staging-v2-admin.escapeplan.ie/login")

    # Enter login details
    login_page.enter_email("admin@escapeplan.com")
    login_page.enter_password("password123")
   
    # Click Sign In
    login_page.click_sign_in()

    # # Wait temporarily so we can inspect what happened
    # page.wait_for_timeout(3000)

   
   #Step 2: Verify dashboard
    # Verify dashboard
    expect(page).to_have_url(
        "https://staging-v2-admin.escapeplan.ie/dashboard"
    )

    #Step 3:
    # Dashboard → Users
    dashboard.click_dashboard()
    dashboard.open_users()
    # Keep browser open for 10 seconds
    hold(page)
            
    dashboard.open_user("full name test")
     # Keep browser open for 10 seconds
    hold(page)
    dashboard.back_to_users()
    # Keep browser open for 10 seconds
    hold(page)
            

    # Users → Dashboard → Proposals
    dashboard.click_dashboard()
    # Keep browser open for 10 seconds
    hold(page)    

    dashboard.open_proposals()
     # Keep browser open for 10 seconds
    hold(page)
            
    dashboard.open_proposal("Automated job title")
    # Keep browser open for 10 seconds
    hold(page)
    
    dashboard.back_to_proposals()
    # Keep browser open for 10 seconds
    hold(page)
            

    # Proposals → Dashboard → Reviews
    dashboard.click_dashboard()
    dashboard.open_pending_reviews()
    hold(page)
    dashboard.open_review("Floor Plan Markup")
    dashboard.back_to_reviews()
    hold(page)

    # Reviews → Dashboard → Printers
    dashboard.click_dashboard()
    hold(page)
    dashboard.open_printers()
    hold(page)
    dashboard.open_printer("sita")
    # Keep browser open for 10 seconds
    hold(page)
            

    # Printers → Dashboard → Technicians
    dashboard.click_dashboard()
    hold(page)
    dashboard.open_technicians()
    hold(page)
    dashboard.open_technician("full name test")
    hold(page)
    dashboard.back_to_technicians()
    hold(page)

    # Technicians → Dashboard → Pricing Plans
    dashboard.click_dashboard()
    hold(page)
    dashboard.open_pricing_plans()
     # Keep browser open for 10 seconds
    hold(page)
    # dashboard.open_first_pricing_plan()
    dashboard.open_pricing_plan("basic plan")
    hold(page)
    dashboard.back_to_pricing_plans()
    hold(page)

    # Pricing Plans → Dashboard
    dashboard.click_dashboard()

    # Keep browser open for 10 seconds
    hold(page)
            