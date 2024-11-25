from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
        link = "http://suninjuly.github.io/alert_accept.html"
        browser = webdriver.Chrome()
        browser.get(link)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        alert = browser.switch_to.alert
        alert.accept()
        txt = browser.find_element(By.ID, "input_value")
        x = txt.text
        input1 = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
        y = calc(x)
        input1.send_keys(y)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        print(browser.switch_to.alert.text.split(': ')[-1])
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()