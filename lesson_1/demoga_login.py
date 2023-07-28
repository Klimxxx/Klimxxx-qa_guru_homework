from selene import browser, have


browser.config.timeout = 40
# для работы следующей строчки необходим установка селениум 4.5.0
browser.config.hold_driver_at_exit = True
browser.open('https://demoqa.com/text-box')

# находим поле инпут фул нейм
browser.element('[id="userName"]').type('Klim').press_tab()

# находим поле инпут имейл
browser.element('[id="userEmail"]').type('123@123.ru').press_tab()

# находим поле инпут курент адрес
browser.element('[id="currentAddress"]').type('Moscow').press_tab()

# находим поле инпут переманент адрес
browser.element('[id="permanentAddress"]').type('PITER').press_tab()

# находим кнопку сабмит
browser.element('[id="submit"]').click()

browser.config.timeout = 2

browser.element('[id="output"] [id="name"]').should(have.text('Klim'))
browser.element('[id="output"] [id="email"]').should(have.text('123@123.ru'))
browser.element('[id="output"] [id="currentAddress"]').should(have.text('Moscow'))
browser.element('[id="output"] [id="permanentAddress"]').should(have.text('PITER'))


