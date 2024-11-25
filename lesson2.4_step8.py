import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    book = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    book.click()
    browser.execute_script("window.scrollBy(0, 100);") # скролл вниз
    txt = browser.find_element(By.ID, "input_value")
    x = txt.text
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    y = calc(x)
    input1.send_keys(y)
    print(y)
    button = browser.find_element(By.ID, "solve")
    button.click()
    alert_obj = browser.switch_to.alert # текст из алерта в консоль
    msg = alert_obj.text
    print(msg)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()