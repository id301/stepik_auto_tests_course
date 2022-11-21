import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
#link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    sum = str(num1 + num2)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(sum)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()