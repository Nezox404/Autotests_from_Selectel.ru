import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class DocsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверка заголовка страницы документации")
    def check_title(self, expected_title):
        WebDriverWait(self.driver, 10).until(lambda d: d.title != "")
        return self.driver.title == expected_title

    @allure.step("Проверка URL страницы документации")
    def check_url_contains(self, expected_part):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(expected_part)
        )
        return expected_part in self.driver.current_url
