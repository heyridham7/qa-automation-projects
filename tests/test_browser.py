import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture

def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_title(driver):
    driver.get("https://books.toscrape.com")
    assert "Books" in driver.title

def test_books_visible(driver):
    driver.get("https://books.toscrape.com")
    books = driver.find_elements(By.CSS_SELECTOR,"article.product_pod")
    assert len(books)>0

def test_price_visible(driver):
    driver.get("https://books.toscrape.com") 
    price = driver.find_element(By.CSS_SELECTOR,"p.price_color")
    assert "£" in price.text