from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/login")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    page.wait_for_url("**/secure")

    # Save cookies, localStorage, sessionStorage
    page.context.storage_state(path="auth.json")

    browser.close()