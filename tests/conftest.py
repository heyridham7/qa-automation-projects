import pytest

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    @pytest.fixture
    def driver():
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield driver
        driver.quit()

except ImportError:
    @pytest.fixture
    def driver():
        return None