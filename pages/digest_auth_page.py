from .base_page import BasePage


class DigestAuthPage(BasePage):
    def authenticate(self, username: str = "admin", password: str = "admin"):
        self.page.goto(f"https://{username}:{password}@the-internet.herokuapp.com/digest_auth", wait_until="load")
        return self
