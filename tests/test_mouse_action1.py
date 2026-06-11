import re
from playwright.sync_api import expect


def test_mouse_hover_hidden_light(page):
    page.goto("https://bootswatch.com/default/")
    page.get_by_role("heading", name="Navbars").click()
    page.locator("#navbarColor01").get_by_role("button", name="Dropdown").click()
    page.get_by_role("link", name="Action", exact=True).click()
    page.locator("#navbarColor01").get_by_role("searchbox", name="Search").click()
    page.locator("#navbarColor01").get_by_role("searchbox", name="Search").fill("abcd")
    page.locator("#navbarColor01").get_by_role("button", name="Search").click()
    page.get_by_role("button", name="Primary").first.click()
    page.get_by_role("button", name="Link").first.click()

    hidden_link = page.get_by_role("button", name="Light").nth(2)
    hidden_link.hover()
    hidden_link.click()
    print("Clicked hidden link")

    page.locator("#btnGroupDrop1").click()
    page.get_by_role("link", name="Dropdown link").first.click()
    page.locator("#btnGroupDrop4").click()
    page.get_by_role("link", name="Dropdown link").nth(1).click()
    page.get_by_role("button", name="Button", exact=True).nth(2).click()
    page.get_by_label("Basic example").get_by_role("button", name="Left").click()
    page.get_by_role("button", name="4").click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(4).click()
    page.locator("#source-modal").press("Escape")
