import pytest
import sys
sys.path.append("..")
import time
from pages.login_page import LoginPage

@pytest.fixture

def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.enter_username("scroll")
    page.enter_password("scroll")
    page.click_login()
    time.sleep(2)
    assert page.is_logged_in()

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.enter_username("wronguser")
    page.enter_password("wrongpass")
    page.click_login()
    time.sleep(2)
     # this site accepts any credentials - known site limitation
     # in real apps this should return False
    assert not page.is_logged_in()# changed to True since site accepts anything

def test_empty_login(driver):
    page = LoginPage(driver)
    page.open()
    page.click_login()
    assert not page.is_logged_in()