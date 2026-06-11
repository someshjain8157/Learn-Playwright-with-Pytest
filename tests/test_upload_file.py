from pathlib import Path
from playwright.sync_api import expect


def test_upload_file(page):
    page.goto("https://the-internet.herokuapp.com/upload")

    page.locator("#file-upload").set_input_files(Path("testdata") / "sample.txt")

    page.locator("#file-submit").click()

    expect(page.get_by_text("File Uploaded!")).to_be_visible()