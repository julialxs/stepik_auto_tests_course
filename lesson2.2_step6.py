from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
        link = "https://suninjuly.github.io/execute_script.html"
        browser = webdriver.Chrome()
        browser.get(link)
        txt = browser.find_element(By.ID, "input_value")
        x = txt.text
        print(x)
        input1 = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
        y = calc(x)
        print(y)
        input1.send_keys(y)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)  # прокручиваем
        input2 = browser.find_element(By.ID, "robotCheckbox").click()
        input3 = browser.find_element(By.ID, "robotsRule").click()

        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()