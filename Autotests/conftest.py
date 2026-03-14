import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.docs_page import DocsPage
from pages.result_page import ResultPage
from config import MAIN_URL


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver, MAIN_URL)


@pytest.fixture
def docs_page(driver):
    return DocsPage(driver)


@pytest.fixture
def kubernetes_page(driver):
    return ResultPage(driver)
