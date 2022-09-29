from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, 'button')
button.click()
confirm = browser.switch_to.alert
confirm.accept()
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
answer = calc(x)
input_element = browser.find_element(By.CSS_SELECTOR, 'input')
input_element.send_keys(answer)
button = browser.find_element(By.CLASS_NAME, "btn btn-primary")
time.sleep(30)
browser.quit()


#alert = browser.switch_to.alert
#alert.accept()

#alert = browser.switch_to.alert
#alert_text = alert.text


prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()