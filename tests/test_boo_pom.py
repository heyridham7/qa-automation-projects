
import pytest
import sys
sys.path.append("..")
from pages.books import BooksPage

@pytest.fixture
def test_title(driver):
    page = BooksPage(driver)
    page.open()
    assert "Books" in page.get_title()

def test_books_visible(driver):
    page = BooksPage(driver)
    page.open()
    books = page.get_book_titles()  
    assert len(books) > 0

def test_price_visible(driver):
    page = BooksPage(driver)
    page.open()
    price = page.get_book_price().text  
    assert "£" in price