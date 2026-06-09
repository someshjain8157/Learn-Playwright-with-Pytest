from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, base_url: str = "https://the-internet.herokuapp.com"):
        self.page = page
        self.base_url = base_url

    def goto_home(self):
        """Open the base site and wait for the page to fully load."""
        self.page.goto(self.base_url, wait_until="load", timeout=20000)
        return self

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


class HomePage(BasePage):
    def goto(self):
        return self.goto_home()

    def click_link_by_name(self, link_text: str):
        self.click_link(link_text)
        return self

    def click_ab_testing(self):
        from .ab_test_page import ABTestPage

        self.click_link("A/B Testing")
        return ABTestPage(self.page)

    def click_add_remove_elements(self):
        from .add_remove_elements_page import AddRemoveElementsPage

        self.click_link("Add/Remove Elements")
        return AddRemoveElementsPage(self.page)

    def click_form_authentication(self):
        from .form_authentication_page import FormAuthenticationPage

        self.click_link("Form Authentication")
        return FormAuthenticationPage(self.page)

    def click_basic_auth(self):
        from .basic_auth_page import BasicAuthPage

        self.click_link("Basic Auth")
        return BasicAuthPage(self.page)
