from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

@given('I am on the login page')
def step_open_login_page(context):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.get("https://quotes.toscrape.com/login")
    time.sleep(2)

@when('I enter username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.driver.find_element(By.NAME, "username").send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)

@when('I click the login button')
def step_click_login(context):
    button = context.driver.find_element(By.CSS_SELECTOR, "input.btn-primary")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
@then('I should be logged in successfully')
def step_verify_login(context):
    try:
        context.driver.find_element(By.LINK_TEXT, "Logout")
        context.driver.quit()
    except:
        context.driver.quit()
        assert False, "Login failed"

@then('I should still be on the login page')
def step_verify_still_on_login(context):
    assert "login" in context.driver.current_url
    context.driver.quit()