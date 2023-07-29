
from selene import be, have
from selene import browser
from selenium import webdriver

browser.config.driver_options = webdriver.ChromeOptions()
browser.config.driver_options.binary_location = (
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
)











browser.config.timeout = 40
browser.config.hold_driver_at_exit = True

browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
