from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    image = browser.find_element(By.CSS_SELECTOR, 'img')
    x = image.get_attribute("valuex")
    result = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(result)
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')
    input2.click()
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]')
    input2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()