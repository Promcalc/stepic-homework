import time
from selenium import webdriver


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/cats.html")
browser.find_element_by_id("button")


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
# 
# Текущую вкладку можно узнать так:
# current_window = browser.current_window_handle
# 
# При открытии новой вкладки WebDriver продолжит работать со старой вкладкой. 
# Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти. 
# Это делается с помощью команды switch_to.window:
# browser.switch_to.window(window_name)
# 
# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, 
# который возвращает массив имён всех вкладок. 
# Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
# new_window = browser.window_handles[1]
# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
# first_window = browser.window_handles[0]
# 
# 
# Улучшим наш тест с помощью неявных ожиданий. 
# Для этого нам нужно будет добавить одну строчку с методом implicitly wait:
# 
# from selenium import webdriver
# 
# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
# 
# browser.get("http://suninjuly.github.io/wait1.html")
# 
# button = browser.find_element_by_id("check")
# button.click()
# message = browser.find_element_by_id("check_message")
# 
# assert "успешно" in message.text
# 
# 
# rom selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# 
# browser = webdriver.Chrome()
# 
# browser.get("http://suninjuly.github.io/wait2.html")
# 
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "check"))
#     )
# button.click()
# message = browser.find_element_by_id("check_message")
# 
# assert "успешно" in message.text
# 
# После выполнения всех действий мы не должны забыть закрыть окно браузера
browser.quit()
