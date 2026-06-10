from playwright.sync_api import Browser

def test_digest_auth(browser: Browser):

    context = browser.new_context(
        http_credentials={
            "username": "admin",
            "password": "admin"
        }
    )

    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/digest_auth", timeout=120000, wait_until="networkidle")

    page.wait_for_timeout(10000) 
    assert "Congratulations" in page.locator("body").text_content()


    context.close()