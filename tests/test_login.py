from pathlib import Path

from dotenv import find_dotenv, load_dotenv
from playwright.sync_api import expect
from cryptography.fernet import Fernet
import os

env_path = find_dotenv()
if not env_path:
    raise FileNotFoundError(".env file not found; please add one to the repository root.")

load_dotenv(dotenv_path=env_path, override=True)


def get_password():
    key = os.getenv("ENCRYPTION_KEY")
    encrypted_password = os.getenv("ENCRYPTED_PASSWORD")

    cipher = Fernet(key.encode())
    password = cipher.decrypt(
        encrypted_password.encode()
    ).decode()

    return password


def test_login_form_submit(page):
    page.goto("https://the-internet.herokuapp.com/login")

    username = os.getenv("USERNAME")
    password = get_password()

    page.locator("#username").fill(username)
    page.locator("#password").fill(password)

    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/secure"
    )

    expect(
        page.get_by_text("You logged into a secure area!")
    ).to_be_visible()

    expect(
        page.get_by_role(
            "heading",
            name="Secure Area",
            exact=True
        )
    ).to_be_visible()