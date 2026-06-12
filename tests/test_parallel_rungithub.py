from playwright.sync_api import Page

def test_github(page: Page):
    page.goto("https://github.com")
    assert "GitHub" in page.title()