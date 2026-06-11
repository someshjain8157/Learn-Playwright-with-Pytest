from playwright.sync_api import Page


def test_dialog_listener(page: Page):

    page.on(
        "dialog",
        lambda dialog: dialog.accept()
    )

    page.goto(
        "https://the-internet.herokuapp.com/javascript_alerts"
    )

    page.get_by_role(
        "button",
        name="Click for JS Alert"
    ).click()