import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    BREADCRUMB_LAST = (By.CSS_SELECTOR, ".breadcrumbs__item:last-child span")
    PAGE_TITLE = (By.CSS_SELECTOR, "h1.page-teaser__title")

    @allure.step("Получить последний элемент хлебных крошек")
    def get_last_breadcrumb(self):
        return self.wait.until(EC.visibility_of_element_located(self.BREADCRUMB_LAST)).text

    @allure.step("Получить заголовок страницы")
    def get_page_header(self):
        return self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE)).text
