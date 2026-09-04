import re
from playwright.sync_api import Page, expect
import pytest


HOLD_MS = 30_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)

# // without csv user file
@pytest.mark.parametrize("userName,password", [
    ("client1@test.com", "password123"),
    ("client2@test.com", "password456")
])

def test_multi_user_login(page: Page,userName: str,password: str) -> None:
  
    page.goto("https://staging-v2-dash.escapeplan.ie/login")
    # hold(page)

    page.goto("https://staging-v2-dash.escapeplan.ie/login")
    page.get_by_role("textbox", name="you@example.com").click()
    page.get_by_role("textbox", name="you@example.com").fill(userName)
    page.get_by_role("textbox", name="••••••••").click()
    page.get_by_role("textbox", name="••••••••").fill(password)
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.get_by_role("button", name="Sign In").click()

     # Assert successful login by validating dashboard redirect.
    expect(page).to_have_url(re.compile(r".*/dashboard/?$"))
    hold(page)
    

