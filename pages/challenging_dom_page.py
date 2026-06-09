from .base_page import BasePage


class ChallengingDOMPage(BasePage):
    @classmethod
    def open(cls, page):
        page.goto("https://the-internet.herokuapp.com/challenging_dom", wait_until="load", timeout=20000)
        return cls(page)

    def get_header_cells(self):
        return self.page.locator("table thead tr th")

    def get_column_index(self, header_name: str) -> int:
        """Return zero-based column index for header text matching `header_name`."""
        headers = self.get_header_cells()
        total = headers.count()
        for i in range(total):
            if headers.nth(i).inner_text().strip() == header_name:
                return i
        raise ValueError(f"Header '{header_name}' not found")

    def get_column_values(self, header_name: str) -> list:
        """Return a list of text values for the column under `header_name`."""
        col_idx = self.get_column_index(header_name) + 1
        cells = self.page.locator(f"table tbody tr td:nth-child({col_idx})")
        return [cells.nth(i).inner_text() for i in range(cells.count())]

    def get_diceret_values(self) -> list:
        """Convenience helper that returns the values under the 'Diceret' header."""
        return self.get_column_values("Diceret")

