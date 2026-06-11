from playwright.sync_api import Page

def test_locator_table(page: Page):
    page.goto("https://the-internet.herokuapp.com", timeout=120000, wait_until="networkidle")

    page.get_by_role("link", name="Challenging DOM").click()

    print(page.url)

    table = page.locator("table")

    column_name = table.locator("thead th").nth(5).inner_text()
    print(f"Column Name: {column_name}")

    #values = table.locator("tbody tr td:nth-child(6)").all_inner_texts()
    #for i, value in enumerate(values, start=0):
    #    print(f"Row {i}: {value}")
   
    rows = table.locator("tbody tr")
    for i in range(rows.count()):
     value = rows.nth(i).locator("td").nth(5).inner_text()
     print(value)