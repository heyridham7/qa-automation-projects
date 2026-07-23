from selenium.webdriver.common.by import By
import time

class LoginPage:
    URL = "https://quotes.toscrape.com/login"

    def __init__(self,driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(self.URL)
        time.sleep(2)
    
    def enter_username(self,username):
        self.driver.find_element(By.NAME,"username").clear()
        self.driver.find_element(By.NAME,"username").send_keys(username)
    
    def enter_password(self,password):
        self.driver.find_element(By.NAME,"password").clear()
        self.driver.find_element(By.NAME,"password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR,"input.btn-primary").click()

    def get_page_title(self):
        return self.driver.title
    
    def is_logged_in(self):
        try:
            self.driver.find_element(By.LINK_TEXT, "Logout")
            return True
        except:
            return False