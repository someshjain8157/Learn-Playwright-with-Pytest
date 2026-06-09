from .base_page import BasePage, HomePage


class AddRemoveElementsPage(BasePage):
    @classmethod
    def open(cls, page):
        home = HomePage(page).goto()
        return home.click_add_remove_elements()

    def get_header_text(self) -> str:
        return self.page.locator("div.example h3").inner_text()

    def click_add_element(self):
        self.page.get_by_role("button", name="Add Element").click()
        return self

    def add_elements(self, count: int = 1):
        for _ in range(count):
            self.click_add_element()
        return self

    def get_delete_button_count(self) -> int:
        return self.page.get_by_role("button", name="Delete").count()

    def has_delete_buttons(self) -> bool:
        return self.get_delete_button_count() > 0

    def click_delete_button(self, index: int = 0):
        delete_buttons = self.page.get_by_role("button", name="Delete")
        delete_buttons.nth(index).click()
        return self

    def delete_all_elements(self):
        while self.has_delete_buttons():
            self.click_delete_button(0)
        return self
