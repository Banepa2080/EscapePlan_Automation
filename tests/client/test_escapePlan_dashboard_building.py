
# Only one time login then create and open building
import re
from datetime import datetime

from playwright.sync_api import Page, expect

from pages.client.escapePlan_dashboard_client_building_page import ClientBuildingPage
from pages.escapePlan_login_page import LoginPage


HOLD_MS = 10_000


def hold(page: Page) -> None:
    page.wait_for_timeout(HOLD_MS)


def test_client_building_flow(page: Page) -> None:
    login_page = LoginPage(page)
    client_building_page = ClientBuildingPage(page)

    # Grant permission
    page.context.grant_permissions(
        ["local-network-access"],
        origin="https://staging-v2-dash.escapeplan.ie",
    )

    # 1. LOGIN
    page.goto("https://staging-v2-dash.escapeplan.ie/login")

    login_page.login(
        "test@gmail.com",
        "test@123",
    )

    expect(page).to_have_url(
        re.compile(r".*/(?:dashboard)/?$")
    )

    # 2. CREATE BUILDING
    building_name = (
        f"Automated building name "
        f"{datetime.now():%Y%m%d%H%M%S}"
    )

    client_building_page.add_building(
        building_name=building_name,
        building_address="123 Test Street, Test City, Test Country",
        building_details="Automated create-building test",
    )

    # After creating the building
    expect(page).to_have_url(
        re.compile(r".*/(?:buildings|create-buildings)/?$")
    )

    # 3. OPEN BUILDINGS
    client_building_page.open_buildings()

    expect(page).to_have_url(
        re.compile(r".*/buildings/?$")
    )

    # 4. VERIFY BUILDING LIST
    expect(page.get_by_role("row").nth(1)).to_be_visible()

    # 5. VIEW LATEST BUILDING
    client_building_page.open_latest_building()

    expect(page).to_have_url(
        re.compile(r".*/buildings/[^/]+/?$")
    )

    # Keep browser open for 10 seconds
    hold(page)






# each time login required :- login then create and again login then open building , so on....
# import re
# from datetime import datetime

# from playwright.sync_api import Page, expect

# from pages.escapePlan_dashboard_client_building_page import ClientBuildingPage
# from pages.escapePlan_login_page import LoginPage


# def test_create_client_building(page: Page) -> None:
#     login_page = LoginPage(page)
#     client_building_page = ClientBuildingPage(page)

#     page.context.grant_permissions(
#         ["local-network-access"],
#         origin="https://staging-v2-dash.escapeplan.ie",
#     )
#     page.goto("https://staging-v2-dash.escapeplan.ie/login")
#     login_page.login("test@gmail.com", "test@123")

#     expect(page).to_have_url(re.compile(r".*/(?:dashboard|create-jobs)/?$"))

#     # A unique name keeps repeated test executions from creating ambiguous records.
#     building_name = f"Automated building name {datetime.now():%Y%m%d%H%M%S}"
#     client_building_page.add_building(
#         building_name=building_name,
#         building_address="123 Test Street, Test City, Test Country",
#         building_details="Automated create-building test",
#     )

#     # The submit action should return the user to the buildings area.
#     expect(page).to_have_url(re.compile(r".*/(?:buildings|create-buildings)/?$"))


# HOLD_MS = 10_000

# def hold(page: Page) -> None:
#     page.wait_for_timeout(HOLD_MS)

# # def test_view_client_building(page: Page) -> None:
# #     login_page = LoginPage(page)
# #     client_building_page = ClientBuildingPage(page)

# #     page.context.grant_permissions(
# #         ["local-network-access"],
# #         origin="https://staging-v2-dash.escapeplan.ie",
# #     )
# #     page.goto("https://staging-v2-dash.escapeplan.ie/login")
# #     login_page.login("test@gmail.com", "test@123")

# #     page.goto("https://staging-v2-dash.escapeplan.ie/buildings")
# #     expect(page).to_have_url(re.compile(r".*/buildings/?$"))
# #     client_building_page.open_building("Automated building name")

# #     expect(page).to_have_url(re.compile(r".*/buildings/[^/]+/?$"))
# #     hold(page)

# # def test_edit_client_building(page: Page) -> None:
# #     login_page = LoginPage(page)
# #     client_building_page = ClientBuildingPage(page)

# #     page.context.grant_permissions(
# #         ["local-network-access"],
# #         origin="https://staging-v2-dash.escapeplan.ie",
# #     )
# #     page.goto("https://staging-v2-dash.escapeplan.ie/login")
# #     login_page.login("test@gmail.com", "test@123")

# #     client_building_page.open_buildings()
# #     client_building_page.open_building("Automated building name")
# #     client_building_page.open_edit_building_form()
# #     expect(page).to_have_url(re.compile(r".*/buildings/[^/]+/edit/?$"))

# #     updated_name = f"Automated building updated {datetime.now():%Y%m%d%H%M%S}"
# #     client_building_page.edit_building(
# #         building_name=updated_name,
# #         address="456 Updated Test Street, Test City, Test Country",
# #         notes="Automated edit-building test",
# #     )

# #     expect(page).to_have_url(re.compile(r".*/buildings/[^/]+/?$"))
# #     expect(page.get_by_role("heading", name=updated_name, exact=True)).to_be_visible()
# #     hold(page)


# # def test_delete_client_building(page: Page) -> None:
# #     login_page = LoginPage(page)
# #     client_building_page = ClientBuildingPage(page)

# #     page.context.grant_permissions(
# #         ["local-network-access"],
# #         origin="https://staging-v2-dash.escapeplan.ie",
# #     )
# #     page.goto("https://staging-v2-dash.escapeplan.ie/login")
# #     login_page.login("test@gmail.com", "test@123")

# #     client_building_page.open_buildings()
# #     client_building_page.open_building("Automated building name")
# #     client_building_page.open_delete_building_modal()

# #     expect(page.get_by_role("button", name="Cancel", exact=True)).to_be_visible()
# #     expect(page.get_by_role("button", name="Delete", exact=True).last).to_be_visible()

# #     client_building_page.confirm_delete_building()

# #     expect(page).to_have_url(re.compile(r".*/buildings/?$"))



# def test_view_client_latest_building(page: Page) -> None:
#     login_page = LoginPage(page)
#     client_building_page = ClientBuildingPage(page)

#     page.context.grant_permissions(
#         ["local-network-access"],
#         origin="https://staging-v2-dash.escapeplan.ie",
#     )
#     page.goto("https://staging-v2-dash.escapeplan.ie/login")
#     login_page.login("test@gmail.com", "test@123")

#     expect(page).to_have_url(re.compile(r".*/(?:dashboard|create-jobs)/?$"))
#     client_building_page.open_buildings()
#     expect(page).to_have_url(re.compile(r".*/buildings/?$"))

#     expect(page.get_by_role("row").nth(1)).to_be_visible()
#     client_building_page.open_latest_building()

#     expect(page).to_have_url(re.compile(r".*/buildings/[^/]+/?$"))
#     hold(page)


# # def test_delete_client_latest_building(page: Page) -> None:
# #     login_page = LoginPage(page)
# #     client_building_page = ClientBuildingPage(page)

# #     page.context.grant_permissions(
# #         ["local-network-access"],
# #         origin="https://staging-v2-dash.escapeplan.ie",
# #     )
# #     page.goto("https://staging-v2-dash.escapeplan.ie/login")
# #     login_page.login("test@gmail.com", "test@123")

# #     expect(page).to_have_url(re.compile(r".*/(?:dashboard|create-jobs)/?$"))
# #     client_building_page.open_buildings()
# #     expect(page).to_have_url(re.compile(r".*/buildings/?$"))

# #     building_rows = page.get_by_role("row")
# #     building_count_before_delete = building_rows.count()
# #     client_building_page.open_latest_building()
# #     expect(page).to_have_url(re.compile(r".*/buildings/[^/]+/?$"))
# #     client_building_page.open_delete_building_modal()
# #     client_building_page.confirm_delete_building()
# #     hold(page)

# #     expect(page).to_have_url(re.compile(r".*/buildings/?$"))
# #     expect(building_rows).to_have_count(building_count_before_delete - 1)

