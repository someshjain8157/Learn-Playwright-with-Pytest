from playwright.sync_api import sync_playwright
import subprocess

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    # Start tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com")

    page.get_by_role("link", name="A/B Testing").click()

    page.wait_for_timeout(2000)

    page.go_back()

    page.get_by_role("link", name="Form Authentication").click()

    page.wait_for_timeout(2000)

    # Stop tracing and save trace
    context.tracing.stop(path="trace.zip")

    browser.close()

# Open Trace Viewer
subprocess.run(["playwright", "show-trace", "trace.zip"])