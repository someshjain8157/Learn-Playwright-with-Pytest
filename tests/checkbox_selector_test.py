from playwright.sync_api import Page

def test_locator_table(page: Page):
    page.goto("https://the-internet.herokuapp.com", timeout=120000, wait_until="networkidle")
    page.get_by_role("link", name="Checkboxes").click()
    page.wait_for_load_state("domcontentloaded", timeout=15000)

    #heading_text = page.get_by_role("heading", name="Checkboxes").wait_for(state="visible", timeout=15000)
    ##print(f"Heading text: {heading_text}")
    checkboxes = page.locator("form#checkboxes input[type='checkbox']")
    checkboxes.nth(0).check()
    checkboxes.nth(1).uncheck()
    page.wait_for_timeout(5000)
    checkboxes.nth(0).set_checked(False)
    checkboxes.nth(1).set_checked(True)
    page.wait_for_timeout(5000)
    


#    page.locator("form#checkboxes input[type='checkbox']").check()
#    page.locator("form#checkboxes input[type='checkbox']").uncheck()
#    page.locator("form#checkboxes input[type='checkbox']").set_checked(True)
#    page.locator("form#checkboxes input[type='checkbox']").set_checked(False)