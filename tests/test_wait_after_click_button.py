from playwright.sync_api import expect

def test_login(page):

    page.goto(
        "https://the-internet.herokuapp.com/login",
        wait_until="domcontentloaded"
    )

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    page.wait_for_url(
        "**/secure",
        wait_until="load"
    )

    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/secure"
    )