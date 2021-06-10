from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button = browser.find_element_by_id("book")
    button.click()

    browser.execute_script("window.scrollBy(0, 100);")

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    test_input = browser.find_element_by_id("answer")
    test_input.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()