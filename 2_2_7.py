import os
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
try:

    browser.get(link)
    input_1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter first name"]')
    input_1.send_keys("Ivan")
    input_2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]')
    input_2.send_keys("Petrov")
    input_3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter email"]')
    input_3.send_keys("ded2393@mail.ru")
    element = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
#file_path = os.path.join(current_dir, 'file.txt')