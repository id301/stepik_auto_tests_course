import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

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