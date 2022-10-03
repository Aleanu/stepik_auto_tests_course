from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, unittest, pytest


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class Test_katya():
    @pytest.mark.parametrize('link_number',
                             ["236895", "236896", "236897", "236898", "236899", "236900", "236903", "236904", "236905"])
    def test_katya2(self, browser, link_number):
        link = f"https://stepik.org/lesson/{link_number}/step/1"
        browser.get(link)
        time.sleep(3)
        #browser.implicity_wait(10)
        answer = math.log(int(time.time()))
        input_area = browser.find_element(By.CSS_SELECTOR, "textarea")
        input_area.send_keys(answer)

        button = browser.find_element(By.CLASS_NAME, "submit-submission")
        button.click()


if __name__ == "__main__":
    unittest.main()



