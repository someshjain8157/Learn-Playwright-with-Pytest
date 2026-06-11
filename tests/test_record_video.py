from playwright.sync_api import sync_playwright

def test_record_complete_browser_video():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            record_video_dir="videos/",
            record_video_size={"width": 1280, "height": 720}
        )

        page = context.new_page()

        page.goto("https://the-internet.herokuapp.com")

        page.get_by_role("link", name="A/B Testing").click()

        page.wait_for_timeout(3000)

        page.go_back()

        page.get_by_role("link", name="Form Authentication").click()

        page.wait_for_timeout(3000)

        context.close()  # IMPORTANT: video is saved only after context closes
        browser.close()