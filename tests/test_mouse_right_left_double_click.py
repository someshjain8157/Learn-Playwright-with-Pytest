from playwright.sync_api import expect


def test_textbox_locators_form(page) -> None:
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://demoqa.com/", timeout=120000, wait_until="networkidle")
    page.get_by_role("link", name="Elements").click()
    page.get_by_role("link", name="Buttons").click()
    page.get_by_role("button", name="Double Click Me").dblclick()
    expect(page.get_by_text("You have done a double click")).to_be_visible()
    page.get_by_role("button", name="Right Click Me", exact=True).click(button="right")
    expect(page.get_by_text("You have done a right click")).to_be_visible()
    page.get_by_role("button", name="Click Me", exact=True).click()
    expect(page.get_by_text("You have done a dynamic click")).to_be_visible()
    print(page.get_by_text("You have done a dynamic click").inner_text())
    print("Test Passed")