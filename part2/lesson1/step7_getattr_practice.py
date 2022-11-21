import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_img = browser.find_element(By.ID, "treasure")
    x = treasure_img.get_attribute("valuex")
    y = calc(x)

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(y)

    robot_chck = browser.find_element(By.ID, 'robotCheckbox')
    robot_chck.click()
    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
