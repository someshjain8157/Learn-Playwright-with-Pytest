import asyncio
import pytest
from playwright.async_api import async_playwright

async def check_title(browser, url):
    page = await browser.new_page()

    await page.goto(url)

    print(f"{url} -> {await page.title()}")

    await page.wait_for_timeout(3000)  # so you can see the page

    await page.close()

@pytest.mark.asyncio
async def test_async_parallel_execution():

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=False
        )

        await asyncio.gather(
            check_title(browser, "https://google.com"),
            check_title(browser, "https://github.com"),
            check_title(browser, "https://bootswatch.com/default/")
        )

        await browser.close()