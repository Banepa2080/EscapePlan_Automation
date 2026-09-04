# from playwright.sync_api import Page, expect

# from pages.admin.escapePlan_dashboard_admin_PDF_review_page import (
#     AdminPDFReviewPage,
# )
# from pages.admin.escapePlan_admin_login_page import LoginPage


# HOLD_MS = 10_000

# def hold(page: Page) -> None:
#     page.wait_for_timeout(HOLD_MS)


# def test_admin_can_review_pdf_files(page: Page) -> None:
#     login_page = LoginPage(page)
#     pdf_review_page = AdminPDFReviewPage(page)

#     # Grant permission
#     page.context.grant_permissions(
#         ["local-network-access"],
#         origin="https://staging-v2-admin.escapeplan.ie",
#     )

#     #Step 1: Open application
#     # Open application
#     page.goto("https://staging-v2-admin.escapeplan.ie/login")

#     # Enter login details
#     login_page.enter_email("admin@escapeplan.com")
#     login_page.enter_password("password123")
   
#     # Click Sign In
#     login_page.click_sign_in()

#     # # Wait temporarily so we can inspect what happened
#     # page.wait_for_timeout(3000)

   
#    #Step 2: Verify dashboard
#     # Verify dashboard
#     expect(page).to_have_url(
#         "https://staging-v2-admin.escapeplan.ie/dashboard"
#     )

#     #Step 3:
#     # Open PDF Review
#     pdf_review_page.click_pdf_review()

#     # Open Evacuation Diagram
#     expect(
#         pdf_review_page.evacuation_diagram_cell
#     ).to_be_visible()

#     pdf_review_page.open_evacuation_diagram()

#     # Keep browser open for 10 seconds
#     hold(page)
    

#     # Go back to PDF Reviews
#     pdf_review_page.back_to_reviews()

#     # Open Floor Plan Markup
#     expect(
#         pdf_review_page.floor_plan_markup_cell
#     ).to_be_visible()

#     pdf_review_page.open_floor_plan_markup()

    
#     # Keep browser open for 10 seconds
#     hold(page)
            

from playwright.sync_api import Page, expect

from pages.admin.escapePlan_dashboard_admin_PDF_review_page import (
    AdminPDFReviewPage,
)
from pages.admin.escapePlan_admin_login_page import LoginPage


HOLD_MS = 10_000

def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)



def test_admin_can_submit_pdf_review(page: Page) -> None:
    pdf_review_page = AdminPDFReviewPage(page)
    login_page = LoginPage(page)
   

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
    # Open PDF Review
    pdf_review_page.click_pdf_review()

    # Open Floor Plan Markup
    pdf_review_page.open_review("Floor Plan Markup")

    # Keep browser open for 10 seconds
    hold(page)

    # Open review details
    pdf_review_page.click_view_review_details()

    # Add review notes
    pdf_review_page.enter_review_notes("add test for review")

    # Keep browser open for 10 seconds
    hold(page)

    # Submit review
    pdf_review_page.submit_review()

    # Return to reviews
    pdf_review_page.back_to_reviews()

    # Keep browser open for 10 seconds
    hold(page)

    # Open Evacuation Diagram
    pdf_review_page.open_review("Evacuation Diagram")

    # Open review details
    pdf_review_page.click_view_review_details()

    # Keep browser open for 10 seconds
    hold(page)
    # Return to reviews
    pdf_review_page.back_to_reviews()

    # Keep browser open for 10 seconds
    hold(page)