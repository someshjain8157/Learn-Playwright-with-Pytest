import pytest
from playwright.async_api import async_playwright

URLS = [
    ("Google", "https://www.google1.com"),
    ("Bing", "https://www.bing.com"),
    ("Yahoo", "https://www.yahoo.com"),
]

@pytest.mark.parametrize("expected,url", URLS)
@pytest.mark.asyncio
async def test_search_engines(expected, url):

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)

        page = await browser.new_page()

        await page.goto(url)

        title = await page.title()

        assert expected in title

        await browser.close()