from playwright.sync_api import Page


def test_response_listener(page: Page):

    responses = []

    def handle_response(response):
        responses.append(response.status)
        print(f"RESPONSE: {response.status}")

    page.on("response", handle_response)

    page.goto("https://the-internet.herokuapp.com")

    assert 200 in responses