import allure
from config import SEARCH_PHRASE, SEARCH_HEADER, NOT_FOUND_PHRASE, RESULT_URL


@allure.feature("Поиск продуктов")
@allure.story("Поиск и навигация")
@allure.title("Поиск 'Кластеры Kubernetes' и переход на страницу продукта")
def test_search_kubernetes(main_page, kubernetes_page):
    main_page.search_for(SEARCH_PHRASE)
    assert main_page.get_results_count() > 0

    main_page.click_first_result()
    assert RESULT_URL in main_page.get_current_url()

    assert kubernetes_page.get_page_header() == SEARCH_HEADER
    assert kubernetes_page.get_last_breadcrumb() == SEARCH_HEADER


@allure.feature("Поиск продуктов")
@allure.story("Поиск и навигация")
@allure.title("Поиск несуществующего продукта")
def test_search_nonexistent(main_page):
    main_page.search_for("qwerty123456789")
    assert main_page.get_empty_search_message() == NOT_FOUND_PHRASE
