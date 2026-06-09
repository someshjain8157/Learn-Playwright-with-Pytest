from .base_page import BasePage


class CheckboxesPage(BasePage):
    @classmethod
    def open(cls, page):
        page.goto("https://the-internet.herokuapp.com/checkboxes", wait_until="load", timeout=20000)
        return cls(page)

    def get_header_text(self) -> str:
        return self.page.locator("h3").inner_text()

    def get_checkboxes(self):
        return self.page.locator("form#checkboxes input[type=checkbox]")

    def get_checkbox_count(self) -> int:
        return self.get_checkboxes().count()

    def get_checkbox(self, index: int = 0):
        return self.get_checkboxes().nth(index)

    def is_checked(self, index: int = 0) -> bool:
        return self.get_checkbox(index).is_checked()

    def click_checkbox(self, index: int = 0):
        self.get_checkbox(index).click()
        return self

    def check(self, index: int = 0):
        checkbox = self.get_checkbox(index)
        if not checkbox.is_checked():
            checkbox.check()
        return self

    def uncheck(self, index: int = 0):
        checkbox = self.get_checkbox(index)
        if checkbox.is_checked():
            checkbox.uncheck()
        return self

    def set_checkbox(self, index: int = 0, value: bool = True):
        return self.check(index) if value else self.uncheck(index)
