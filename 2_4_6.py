import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
browser.execute_script("window.scrollBy(0, 200);")
button = browser.find_element(By.ID, 'book')
button.click()
browser.execute_script("window.scrollBy(0, 500);")
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
answer = calc(x)
input_element = browser.find_element(By.CSS_SELECTOR, 'input')
input_element.send_keys(answer)
button = browser.find_element(By.ID, "solve")
button.click()
time.sleep(30)
#message = browser.find_element(By.ID, "verify_message")
#assert "successful" in message.text