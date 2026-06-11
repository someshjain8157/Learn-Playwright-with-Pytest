from playwright.sync_api import expect


def test_textbox_locators_form(page) -> None:
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://demoqa.com/", timeout=120000, wait_until="networkidle")
    page.get_by_role("link", name="Elements").click()
    page.get_by_text("Check Box").click()
    # page.locator(".rc-tree-switcher").nth(0).click()
    page.get_by_role("checkbox", name="Home").locator("..").locator(".rc-tree-switcher").click()
    #home = page.get_by_role("treeitem", name="Home")
    #home.locator(".rc-tree-switcher").click()
    page.get_by_role("checkbox", name="Select Downloads").locator("..").locator(".rc-tree-switcher").click()
    page.get_by_role("checkbox", name="Select Downloads").check()
    expect(page.get_by_role("checkbox", name="Select Downloads")).to_be_checked()
