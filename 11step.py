from selenium import webdriver

import time


link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
try:

    browser.get(link)

    input_1 = browser.find_element(by='css selector', value='input.form-control.first:required')
    input_1.send_keys("Ivan")
    time.sleep(3)
    input_2 = browser.find_element(by='css selector', value='input.form-control.second:required')
    input_2.send_keys("Petrov")
    time.sleep(3)
    input_3 = browser.find_element(by='css selector', value='input.form-control.third:required')
    input_3.send_keys("Smolensk")

    time.sleep(3)
    # Отправляем заполненную форму
    button = browser.find_element(by='css selector', value='button.btn')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(by='tag name', value='h1')
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()