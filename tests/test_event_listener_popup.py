from playwright.sync_api import Page


def test_popup_listener(page: Page):

    popup_pages = []

    page.on(
        "popup",
        lambda popup: popup_pages.append(popup)
    )

    page.goto(
        "https://the-internet.herokuapp.com/windows"
    )

    page.get_by_role(
        "link",
        name="Click Here"
    ).click()

    assert len(popup_pages) == 1