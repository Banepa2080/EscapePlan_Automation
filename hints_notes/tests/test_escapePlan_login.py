import re
from playwright.sync_api import Page, expect
from pages.escapePlan_login_page import LoginPage


HOLD_MS = 30_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)
# # By codegen // without page object model
# def test_example(page: Page) -> None:
#     page.goto("https://staging-v2-dash.escapeplan.ie/login")
#     page.get_by_role("textbox", name="you@example.com").click()
#     page.get_by_role("textbox", name="you@example.com").fill("client1@test.com")
#     page.get_by_role("textbox", name="••••••••").click()
#     page.get_by_role("textbox", name="••••••••").fill("password123")
#     page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
#     page.get_by_role("button", name="Sign In").click()


# modify by me // with page object model
def test_successful_login_redirects_to_dashboard(page: Page) -> None:
    login_page = LoginPage(page)

    page.goto("https://staging-v2-dash.escapeplan.ie/login")
    # hold(page)

    login_page.enter_emailAddress("test@gmail.com")
    # hold(page)

    login_page.enter_password("test@123")
    hold(page)

    login_page.click_login()
    hold(page)

    # Assert successful login by validating dashboard redirect.
    expect(page).to_have_url(re.compile(r".*/dashboard/?$"))
    hold(page)

