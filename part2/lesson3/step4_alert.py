import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_to_init_alert = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    button_to_init_alert.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    y_field = browser.find_element(By.ID, 'answer')
    y_field.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    button.click()


finally:
    time.sleep(10)
    browser.quit()