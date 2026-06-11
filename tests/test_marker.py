import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login(page):
    pass


@pytest.mark.regression
def test_invalid_login(page):
    pass


@pytest.mark.sanity
def test_forgot_password(page):
    pass