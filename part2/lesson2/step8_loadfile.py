import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_fname = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    input_fname.send_keys('Nikolay')
    input_lname = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    input_lname.send_keys('Surname')
    input_email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    input_email.send_keys('Email')

    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'bio.txt') # добавляем к этому пути имя файла

    input_file = browser.find_element(By.ID, 'file')
    input_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()