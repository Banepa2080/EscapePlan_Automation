# Test	                    Data	                    Expected Result
# Valid Login	Correct email + correct password	Redirect to Dashboard

# import re

# from playwright.sync_api import Page, expect

# from pages.escapePlan_login_page import LoginPage


# BASE_URL = "https://staging-v2-dash.escapeplan.ie"


# HOLD_MS = 10_000
# def hold(page: Page) -> None:
#     page.wait_for_timeout(HOLD_MS)


# def test_valid_login(page: Page) -> None:
#     login_page = LoginPage(page)

#     # Open login page
#     login_page.navigate_to_login()

#     # Login using valid credentials
#     login_page.login(
#         "test@gmail.com",
#         "test@123"
#     )

#     # Verify successful login
#     expect(page).to_have_url(
#         re.compile(r".*/dashboard/?$")
#     )


#     hold(page)




# # Invalid login tests
# # For invalid data, parametrization is much better than creating a separate test for every combination.
# Test	                    Data	                      Expected Result
# In-Valid Login	In-Correct email + incorrect password	  Fail to redirect to Dashboard

import pytest

from playwright.sync_api import Page, expect

from pages.escapePlan_login_page import LoginPage



HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


@pytest.mark.parametrize(
    "email,password,test_case",
    [
        (
            "wrong@gmail.com",
            "test@123",
            "Invalid Email"
        ),
        (
            "test@gmail.com",
            "wrongpassword",
            "Invalid Password"
        ),
        (
            "wrong@gmail.com",
            "wrongpassword",
            "Invalid Email and Password"
        ),
        (
            "",
            "test@123",
            "Blank Email"
        ),
        (
            "test@gmail.com",
            "",
            "Blank Password"
        ),
        (
            "",
            "",
            "Blank Email and Password"
        ),
        (
            "invalid-email",
            "test@123",
            "Invalid Email Format"
        ),
        (
             "test@gmail.com",
             "test@123",
            "Valid Email Format"
        ),
    ]
)
def test_invalid_login(
    page: Page,
    email: str,
    password: str,
    test_case: str
) -> None:

    login_page = LoginPage(page)

    # Open login page
    login_page.navigate_to_login()

    # Attempt login
    login_page.login(email, password)


  
    # Login should NOT redirect to dashboard
    expect(page).not_to_have_url(
        "https://staging-v2-dash.escapeplan.ie/dashboard"
    )

    hold(page)





# import re
# from playwright.sync_api import Page, expect
# from pages.escapePlan_login_page import LoginPage


# HOLD_MS = 30_000


# def hold(page: Page) -> None:
#     page.wait_for_timeout(HOLD_MS)
# # # By codegen // without page object model
# # def test_example(page: Page) -> None:
# #     page.goto("https://staging-v2-dash.escapeplan.ie/login")
# #     page.get_by_role("textbox", name="you@example.com").click()
# #     page.get_by_role("textbox", name="you@example.com").fill("client1@test.com")
# #     page.get_by_role("textbox", name="••••••••").click()
# #     page.get_by_role("textbox", name="••••••••").fill("password123")
# #     page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
# #     page.get_by_role("button", name="Sign In").click()


# # modify by me // with page object model
# def test_successful_login_redirects_to_dashboard(page: Page) -> None:
#     login_page = LoginPage(page)

#     page.goto("https://staging-v2-dash.escapeplan.ie/login")
#     # hold(page)

#     login_page.enter_emailAddress("test@gmail.com")
#     # hold(page)

#     login_page.enter_password("test@123")
#     hold(page)

#     login_page.click_login()
#     hold(page)

#     # Assert successful login by validating dashboard redirect.
#     expect(page).to_have_url(re.compile(r".*/dashboard/?$"))
    #     hold(page)

