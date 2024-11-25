from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("first_name")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("last_name")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("city")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("country")
    driver = browser.find_element(By.XPATH, "//button[text()='Submit']").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()