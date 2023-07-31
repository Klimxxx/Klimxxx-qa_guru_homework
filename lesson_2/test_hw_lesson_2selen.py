
from selene.support.shared import browser
from selene import be, have, browser
import pytest
from selenium import webdriver



browser.config.driver_options = webdriver.ChromeOptions()
browser.config.driver_options.binary_location = (
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')

url = 'https://google.com'

@pytest.fixture()
def window_change():
    # устанавливаем таймаут у браузера - 10 сек для нестабильного интернета
    browser.config.timeout = 10
    # удерживаем браузер открытым после выполнения теста
    #browser.config.hold_driver_at_exit = True
    # меняем размеры браузера
    browser.config.window_height = 1000
    browser.config.window_width = 1000
    # открываем браузер по урл
    browser.open(url)
    yield browser
    # закрываем браузер после каждого теста
    browser.quit()
def test_check_result(window_change):
    assert browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python')), "Результаты содержат текст..."

def test_check_no_result(window_change):
    assert browser.element('[name="q"]').should(be.blank).type('aslkdhaslgha;lsdhgal;dsg').press_enter()
    assert browser.element('[id="res"]').should(have.text('No results containing all your search terms were found.')), "Проверка что нет результатов"
