from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:

    x = browser.find_element(By.ID, "input_value").text
    x = int(x)
    answer = calc(x)
    browser.execute_script("window.scrollBy(0, 200);")
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(answer)
    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()
    input2 = browser.find_element(By.ID, 'robotsRule')
    input2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
#browser.find_element(By.TAG_NAME, "select").click()
#browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    #browser.find_element(By.CSS_SELECTOR, "[value=$answer]").click()

    #select = Select(browser.find_element(By.TAG_NAME, "select"))
    #select.select_by_value(str(answer)) # ищем элемент с текстом
    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()













#from selenium import webdriver
from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()
#link = "https://SunInJuly.github.io/execute_script.html"
#browser.get(link)
#button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#browser.execute_script("window.scrollBy(0, 100);")
#button.click()