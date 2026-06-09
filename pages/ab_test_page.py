from .base_page import BasePage, HomePage


class ABTestPage(BasePage):
    @classmethod
    def open(cls, page):
        home = HomePage(page).goto()
        return home.click_ab_testing()

    def get_header_text(self) -> str:
        return self.page.locator("h3").inner_text()

    def get_description_text(self) -> str:
        return self.page.locator(".example p").inner_text()

    def get_footer_link_text(self) -> str:
        return self.page.get_by_role("link", name="Elemental Selenium").inner_text()

    def get_footer_link_href(self) -> str:
        return self.page.get_by_role("link", name="Elemental Selenium").get_attribute("href")

    def click_elemental_selenium(self):
        return self.click_link_in_popup("Elemental Selenium")
