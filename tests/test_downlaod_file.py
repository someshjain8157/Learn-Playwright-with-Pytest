from pathlib import Path
from playwright.sync_api import expect


def test_download_file(page):
    page.goto("https://the-internet.herokuapp.com/download")

    with page.expect_download() as download_info:
        page.get_by_role("link", name="sample.txt", exact=True).click()

    download = download_info.value
    repo_root = Path(__file__).resolve().parents[1]
    target_dir = repo_root / "downloadedfiles"
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / download.suggested_filename
    download.save_as(str(target))

    assert target.exists()