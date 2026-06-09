import os
import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def browser_launch_args():
    return {
        "headless": True,
        "slow_mo": 2000,  # 1 second delay per action
    }



@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    ctx_args = {**browser_context_args}
    auth_file = "auth.json"
    if os.path.exists(auth_file):
        ctx_args["storage_state"] = auth_file
    return ctx_args