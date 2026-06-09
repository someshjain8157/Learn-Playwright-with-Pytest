from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, base_url: str = "https://the-internet.herokuapp.com"):
        self.page = page
        self.base_url = base_url

    def goto_home(self):
        """Open the base site and wait for the page to fully load."""
        self.page.goto(self.base_url, wait_until="load", timeout=20000)
        return self

    def goto(self):
        """Alias for compatibility with page objects that use goto()."""
        return self.goto_home()

    def click_ab_testing(self):
        """Click the A/B Testing link from the home page and return the ABTestPage."""
        from .ABTestPage import ABTestPage

        self.click_link("A/B Testing")
        return ABTestPage(self.page)

    def get_link(self, link_text: str):
        return self.page.get_by_role("link", name=link_text)

    def click_link(self, link_text: str, timeout: int = 15000):
        """Click a link that navigates in the current tab."""
        link = self.get_link(link_text)
        with self.page.expect_navigation(wait_until="load", timeout=timeout):
            link.click()
        return self.page

    def click_link_in_popup(self, link_text: str, timeout: int = 15000):
        """Click a link that opens a new tab/window and return the popup page."""
        link = self.get_link(link_text)
        with self.page.expect_popup(timeout=timeout) as popup_info:
            link.click()
        popup = popup_info.value
        popup.wait_for_load_state("load", timeout=timeout)
        return popup

    def get_link_href(self, link_text: str) -> str:
        return self.get_link(link_text).get_attribute("href")
