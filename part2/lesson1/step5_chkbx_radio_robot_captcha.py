import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(y)

    robot_chck = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    robot_chck.click()
    robot_radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    robot_radio.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()