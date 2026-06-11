from playwright.sync_api import expect

def test_networkidle(page):
    page.goto(
        "https://demo.playwright.dev/todomvc",
        wait_until="load"
    )

    expect(
        page.get_by_placeholder(
            "What needs to be done?"
        )
    ).to_be_visible()