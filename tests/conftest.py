import pytest
import subprocess
import os


import subprocess


def pytest_sessionfinish(session, exitstatus):
    try:
        subprocess.run(
            [
                "allure.bat",
                "generate",
                "allure-results",
                "-o",
                "allure-report",
                "--clean"
            ],
            shell=True,
            check=True
        )

        print("\n✅ Allure HTML generated: allure-report/index.html")

    except Exception as e:
        print(f"\n❌ Allure generation failed: {e}")


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "slow_mo": 2000,
    }
