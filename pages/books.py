from selenium.webdriver.common.by import By

class BooksPage:

    url = "https://books.toscrape.com"

    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title
    
    def get_book_titles(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    def get_book_price(self):
        return self.driver.find_element(By.CSS_SELECTOR,"p.price_color")
    

