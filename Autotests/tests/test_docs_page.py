import allure
from config import DOCS_TITLE, DOCS_LINK


@allure.feature("Документация")
@allure.story("Переход по ссылке")
@allure.title("Проверка открытия страницы документации после клика")
def test_documentation_link(main_page, docs_page):
    main_page.click_documentation()
    main_page.switch_to_new_window()

    assert DOCS_LINK in docs_page.get_current_url()
    assert docs_page.get_page_title() == DOCS_TITLE
