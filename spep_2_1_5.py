import time
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/math.html")
time.sleep(2)

x_element = browser.find_element_by_id("input_value")
check_element = browser.find_element_by_id("robotCheckbox")
radio_element = browser.find_element_by_id("robotsRule")
text_element = browser.find_element_by_id("answer")
submit_button = browser.find_element_by_css_selector('[type="submit"]')

x = x_element.text
y = calc(x)


check_element.click();
radio_element.click();

text_element.send_keys(y)


submit_button.click()
time.sleep(15)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
browser.quit()
