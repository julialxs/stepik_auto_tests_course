from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
        link = "http://suninjuly.github.io/file_input.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, "input[name=firstname]")
        input1.send_keys("test")
        input2 = browser.find_element(By.CSS_SELECTOR, "input[name=lastname]")
        input2.send_keys("test")
        input3 = browser.find_element(By.CSS_SELECTOR, "input[name=email]")
        input3.send_keys("test")
        current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        with open("test.txt", "w") as file:
                content = file.write("automationbypython")  # create test.txt file
        file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
        element = browser.find_element(By.ID, "file")
        element.send_keys(file_path)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()