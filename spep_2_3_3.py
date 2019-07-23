import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

sname = "Имя"
sfam = "Фамилия"
semail = "email@mail.ru"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'auto.txt')

file1 = open(file_path,"w")
file1.writelines([sname, "\n", sfam, "\n", semail, "\n"])
file1.close()


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/file_input.html")
time.sleep(1)

input_name = browser.find_element_by_css_selector('[name="firstname"]')
input_fam = browser.find_element_by_css_selector('[name="lastname"]')
input_email = browser.find_element_by_css_selector('[name="email"]')
input_file = browser.find_element_by_css_selector('[type="file"]')

input_name.send_keys(sname)
input_fam.send_keys(sfam)
input_email.send_keys(semail)

input_file.send_keys(file_path)

submit_button = browser.find_element_by_css_selector('[type="submit"]')

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
# 
# import os 
# 
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
# element.send_keys(file_path)
# alert = browser.switch_to.alert
# alert.accept()
# Чтобы получить текст из alert, используйте свойство text объекта alert:
# 
# alert = browser.switch_to.alert
# alert_text = alert.text
# метод для отказа: alert.dismiss()
# 
# Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys():
# 
# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()

# После выполнения всех действий мы не должны забыть закрыть окно браузера
browser.quit()
