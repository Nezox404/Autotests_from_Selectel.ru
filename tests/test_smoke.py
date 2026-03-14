import pytest
import allure
from config import MAIN_TITLE


@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Проверка заголовка главной страницы")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    assert main_page.get_page_title() == MAIN_TITLE
