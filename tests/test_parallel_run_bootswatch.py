from playwright.sync_api import Page

def test_bootswatch(page: Page):
    page.goto("https://bootswatch.com/default/")
    assert page.get_by_role("heading", name="Default").text_content() == "Default"