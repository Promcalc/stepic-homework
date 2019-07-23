import time
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/get_attribute.html")
time.sleep(2)

x_element = browser.find_element_by_id("treasure")
check_element = browser.find_element_by_id("robotCheckbox")
radio_element = browser.find_element_by_id("robotsRule")
text_element = browser.find_element_by_id("answer")
submit_button = browser.find_element_by_css_selector('[type="submit"]')


# human_radio = browser.find_element_by_id("humanRule")
# human_checked = human_radio.get_attribute("checked")
# print("value of human radio: ", human_checked)
# assert human_checked is not None, "Human radio is not selected by default"

# browser.find_element_by_tag_name("select").click()
# browser.find_element_by_css_selector("option:nth-child(2)").click()
# Последняя строчка может выглядеть и так:
# 
# browser.find_element_by_css_selector("[value='1']").click()
# Это не самый удобный способ, так как нам приходится делать лишний клик для открытия списка.
# 
# Есть более удобный способ, для которого используется специальный класс Select из библиотеки WebDriver. Вначале мы должны инициализировать новый объект, передав в него WebElement с тегом select. Далее можно найти любой вариант из списка с помощью метода select_by_value(value):
# 
# from selenium.webdriver.support.ui import Select
# select = Select(browser.find_element_by_tag_name("select"))
# select.select_by_value("1") # ищем элемент с текстом "Python"
# 
# select.select_by_visible_text("text")
# select.select_by_index(index)
# select.select_by_visible_text("Python")

x = x_element.get_attribute("valuex")
y = calc(x)


check_element.click();
radio_element.click();

text_element.send_keys(y)


submit_button.click()
time.sleep(15)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
browser.quit()
