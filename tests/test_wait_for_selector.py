def test_wait_for(page):

    page.goto(
        "https://the-internet.herokuapp.com/dynamic_loading/1"
    )

    page.get_by_role(
        "button",
        name="Start"
    ).click()

    page.locator(
        "#finish"
    ).wait_for(
        state="visible"
    )
    print("1st test is executed.")


def test_wait_for_selector(page):

    page.goto(
        "https://the-internet.herokuapp.com/dynamic_loading/1"
    )

    page.get_by_role(
        "button",
        name="Start"
    ).click()

    page.wait_for_selector(
        "#finish",
        state="visible"
    )
    print("2nd test is executed.")