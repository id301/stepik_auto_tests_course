import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  browser.get("http://suninjuly.github.io/explicit_wait2.html")

  price_label = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
  book_button = browser.find_element(By.ID, 'book')
  book_button.click()

  x = browser.find_element(By.ID, 'input_value')
  y = calc(x.text)
  y_field = browser.find_element(By.ID, 'answer')
  y_field.send_keys(y)
  solve_button = browser.find_element(By.ID, 'solve')
  solve_button.click()

finally:
  time.sleep(10)
  browser.quit()
