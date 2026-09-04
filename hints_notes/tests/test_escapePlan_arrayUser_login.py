import json
import re
import csv
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

# Hold for 10 seconds
HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)



# # Path(__file__).parent.parent / "fake_User_for_loginTest" / "test_user.csv" ===> This means:
# Path(__file__) → test_escapePlan_arrayUser_login.py
# .parent → tests
# .parent → EscapePlan_Automation
# then → fake_User_for_loginTest/test_user.csv

# Read users from CSV file
def get_csv_data() -> list:
    csv_file = (
        Path(__file__).parent.parent
        / "fake_User_for_loginTest"
        / "test_user.csv"
    )

    data = []

    with open(csv_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            # if len(row) >= 2:
            #     data.append((row[0], row[1]))
            data.append(row)
    return data
# @pytest.mark.parametrize("userName,password", get_csv_data())

 # OR for Json file 
 # there are three ways to read the data from json file and use it in test case.

# 1. # read user from json file
# def get_json_data() -> list:
#     json_file = (
#         Path(__file__).parent.parent
#         / "fake_User_for_loginTest"
#         / "test_user.json"
#     )
 
#     with open(json_file, "r") as jsonfile:
#         reader = json.load(jsonfile)
#     return reader

# 2. 
# def get_json_data() -> list:
#     json_file = (
#         Path(__file__).parent.parent
#         / "fake_User_for_loginTest"
#         / "test_user.json"
#     )

#     with open(json_file, "r", encoding="utf-8") as jsonfile:
#         return json.load(jsonfile)

# @pytest.mark.parametrize(
#     "userName,password",
#     [
#         (user["username"], user["password"])
#         for user in get_json_data()
#     ]
# )


# # 3.  OR
def get_json_data() -> list:
    json_file = (
        Path(__file__).parent.parent
        / "fake_User_for_loginTest"
        / "test_user.json"
    )

    with open(json_file, "r", encoding="utf-8") as jsonfile:
        users = json.load(jsonfile)

    return [
        (item["username"], item["password"])
        for item in users
    ]

@pytest.mark.parametrize("userName,password", get_json_data())
def test_multi_user_login(
    page: Page,
    userName: str,
    password: str
) -> None:

    # Open login page
    page.goto("https://staging-v2-dash.escapeplan.ie/login")

    # Enter username/email
    page.get_by_role(
        "textbox",
        name="you@example.com"
    ).fill(userName)

    # Enter password
    page.get_by_role(
        "textbox",
        name="••••••••"
    ).fill(password)

    # Click Sign In
    page.get_by_role(
        "button",
        name="Sign In"
    ).click()

    # Verify successful login
    expect(page).to_have_url(
        re.compile(r".*/dashboard/?$")
    )

    # Keep browser open for 30 seconds
    hold(page)