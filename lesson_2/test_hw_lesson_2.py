import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


link = "https://google.com"

@pytest.fixture()
def browser():
    # обозначаем драйвер перед каждым тестом
    driver = webdriver.Chrome()
    yield driver
    # закрываем браузер после каждого теста
    driver.quit()
@pytest.fixture()
def change_window_size(browser):
    # открываем адрес в браузере
    browser.get(link)
    # устанавливаем нужные размеры браузера
    browser.set_window_size(1000, 1000)

def test_check_result(browser, change_window_size):
    # устанавливаем время ожидания элементов 5 сек
    browser.implicitly_wait(5)
    # ищем строку поиска, клик, вводим текст, нажимаем enter
    input_search = browser.find_element(By.NAME, "q")
    input_search.click()
    input_search.send_keys("yashaka/selene")
    input_search.send_keys(Keys.ENTER)
    # ищем результаты поиска по айди
    result_search = browser.find_element(By.ID, "search")
    text = result_search.text
    # проверяем, что текст есть в результатах поиска
    assert 'Selene - User-oriented Web UI browser tests in Python' in text, "Текст не найден в результатах поиска"
def test_check_no_result(browser, change_window_size):
    # устанавливаем время ожидания элементов 5 сек
    browser.implicitly_wait(5)
    # ищем строку поиска, клик, вводим текст, нажимаем enter
    input_search = browser.find_element(By.NAME, "q")
    input_search.click()
    input_search.send_keys("aslkdhaslgha;lsdhgal;dsg")
    input_search.send_keys(Keys.ENTER)
    # ищем результаты поиска по айди
    result_search_2 = browser.find_element(By.ID, "res")
    text = result_search_2.text
    # проверяем, что текст есть в результатах поиска
    assert 'No results containing all your search terms were found.' in text, "Проверка что нет результатов в данном запросе"

