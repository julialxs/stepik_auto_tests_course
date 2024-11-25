import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
radio = browser.find_element(By.ID, "robotsRule") # находим элемент
browser.execute_script("return arguments[0].scrollIntoView(true);", radio) # прокручиваем
radio.click()
time.sleep(10)