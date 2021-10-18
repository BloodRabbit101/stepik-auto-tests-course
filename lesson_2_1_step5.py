from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    b = webdriver.Chrome()
    b.get(link)
    x_element = b.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = b.find_element_by_id("answer")
    input1.send_keys(y)
    option2 = b.find_element_by_id("robotCheckbox")
    option2.click()
    option3 = b.find_element_by_id("robotsRule")
    option3.click()
    button = b.find_element_by_xpath("//button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    b.quit()

# не забываем оставить пустую строку в конце файла