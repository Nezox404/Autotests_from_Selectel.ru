import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)


    PRODUCTS_BUTTON = (By.CSS_SELECTOR, "button[data-qa='main-nav__group-products']")
    PRODUCTS_DROPDOWN = (By.CSS_SELECTOR, ".nav-dropdown")
    SEARCH_INPUT = (By.CSS_SELECTOR, ".nav-dropdown__search-field input.ant-input")
    DOCUMENTATION_LINK = (By.CSS_SELECTOR, "a[data-qa='main-nav__link-documentation']")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".nav-dropdown__links--searching-results .menu-link")
    FIRST_SEARCH_RESULT = (By.CSS_SELECTOR, ".nav-dropdown__links--searching-results .menu-link__title")
    EMPTY_SEARCH_MESSAGE = (By.CSS_SELECTOR, ".searching-results__empty div")

    @allure.step("Клик по ссылке 'Документация'")
    def click_documentation(self):
        self.wait.until(EC.element_to_be_clickable(self.DOCUMENTATION_LINK)).click()

    @allure.step("Клик по кнопке 'Продукты'")
    def click_products(self):
        button = self.wait.until(EC.element_to_be_clickable(self.PRODUCTS_BUTTON))
        button.click()
        self.wait.until(EC.visibility_of_element_located(self.PRODUCTS_DROPDOWN))

    @allure.step("Поиск продукта")
    def search_for(self, text):
        self.click_products()
        popup = self.wait.until(EC.visibility_of_element_located(self.PRODUCTS_DROPDOWN))

        search = self.driver.execute_script("""
            return arguments[0].querySelector('input[type="search"]');
        """, popup)

        self.driver.execute_script("""
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('input', {bubbles: true}));
            arguments[0].focus();
            arguments[0].click();
        """, search, text)

        self.wait.until(lambda d: len(d.find_elements(*self.SEARCH_RESULTS)) > 0 or
                                  len(d.find_elements(*self.EMPTY_SEARCH_MESSAGE)) > 0)

    @allure.step("Получение количества результатов поиска")
    def get_results_count(self):
        return len(self.wait.until(EC.presence_of_all_elements_located(self.SEARCH_RESULTS)))

    @allure.step("Клик по первому результату")
    def click_first_result(self):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_SEARCH_RESULT)).click()

    @allure.step("Получение текста сообщения при пустом поиске")
    def get_empty_search_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.EMPTY_SEARCH_MESSAGE)).text
