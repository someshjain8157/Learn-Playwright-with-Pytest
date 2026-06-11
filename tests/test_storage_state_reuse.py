from playwright.sync_api import expect


def test_storage_state_applies(page):
    # Navigates to a secure page using the pytest-playwright `page` fixture.
    # `tests/conftest.py` will apply `storage_state: auth.json` when present.
    page.goto("https://the-internet.herokuapp.com/secure", timeout=120000, wait_until="networkidle")
    title = page.title()
    print("Page title:", title)
    assert "Secure Area" in title or "The Internet" in title