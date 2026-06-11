from datetime import datetime
from playwright.sync_api import Page


def test_ab_testing_screenshot(page: Page):
    page.goto("https://the-internet.herokuapp.com")

    page.get_by_role("link", name="A/B Testing").click()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    page.screenshot(
        path=f"screenshots/homepage_{timestamp}.png",
        full_page=True
    )