from playwright.sync_api import sync_playwright

config = {
    "headless": False,
    "slow_mo": 1000,
    "timeout": 30000,  # 30 seconds
    "viewport": {"width": 1280, "height": 720},
}