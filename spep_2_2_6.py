import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/execute_script.html")
time.sleep(1)

x1 = browser.find_element_by_id("input_value").text

check_element = browser.find_element_by_id("robotCheckbox")
radio_element = browser.find_element_by_id("robotsRule")
text_element = browser.find_element_by_id("answer")
submit_button = browser.find_element_by_css_selector('[type="submit"]')

y=calc(x1)


browser.execute_script("return arguments[0].scrollIntoView(true);", check_element)
check_element.click();

browser.execute_script("return arguments[0].scrollIntoView(true);", radio_element)
radio_element.click();

text_element.send_keys(y)

browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()
time.sleep(15)

# browser.execute_script("alert('Robots at work');")
# browser.execute_script('document.title="Script executing";')
# element = browser.execute_script('document.getElementsByName("name")')
# getElementById
# getElementsByTagName
# getElementsByClassName
# querySelector - для CSS
# querySelectorAll - для CSS (находит все совпадения)
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
# button = document.getElementsByTagName("button")[0];
# button.scrollIntoView();
#
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
# Есть более удобный способ, для которого используется специальный класс Select из библиотеки WebDriver. 
# Вначале мы должны инициализировать новый объект, передав в него WebElement с тегом select.
# Далее можно найти любой вариант из списка с помощью метода select_by_value(value):
# 
# from selenium.webdriver.support.ui import Select
# select = Select(browser.find_element_by_tag_name("select"))
# select.select_by_value("1") # ищем элемент с текстом "Python"
# 
# select.select_by_visible_text("text")
# select.select_by_index(index)
# select.select_by_visible_text("Python")

# После выполнения всех действий мы не должны забыть закрыть окно браузера
browser.quit()
