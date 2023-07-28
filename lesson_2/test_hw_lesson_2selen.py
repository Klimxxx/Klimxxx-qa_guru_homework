
#ДАННЫЙ ЧЕРНОВИК С ПОМОЩЬЮ СЕЛЕНА, НЕТ ВОЗМОЖНОСТИ ПРОВЕРИТЬ, ИЗЗА НЕРАБОТОСПОСОБНОСТИ СЕЛЕНА С НОВОЙ ВЕРСИЕЙ БРАУЗЕРА ХРОМ
from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture()
def browser_1():
    browser.config.timeout = 10
    #browser.config.hold_driver_at_exit = True
    browser.open('https://google.com')

@pytest.fixture()
def test_change_window(browser_1):
    print("Called before each test")
    # browser.config.window_width(500)
    # browser.config.window_height(500)
def test_first(browser_1, change_window):
    assert browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python')), "Результаты содержат текст..."

