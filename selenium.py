#selenium is a web automation tool that can be used to automate web browsers. It is also used to scrape data from websites.
# The selenium package is used to automate web browser interaction from Python.
import time

from selenium import webdriver
from selenium.webdriver import Keys

# The webdriver module provided by Selenium provides all the WebDriver implementations.
# Currently supported WebDriver implementations are Firefox, Chrome, IE and Remote. The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.

#example
driver = webdriver.Chrome()

#get url
# driver.get("https://omayo.blogspot.com/")

#find element by id
# element = driver.find_element('id', 'element_id')

# driver.get('https://omayo.blogspot.com/')
# element = driver.find_element('id', 'multiselect1')
# element.click()





#find element by name
# element = driver.find_element('name', 'element_name')
# driver.get('https://omayo.blogspot.com/')
# element = driver.find_element('name', 'userid')
# element.send_keys('admin')

# time.sleep(5)

#find element by xpath
# element = driver.find_element('xpath', 'element_xpath')
# driver.get('https://omayo.blogspot.com/')
# element = driver.find_element('xpath', '//*[@id="multiselect1"]/option[1]')
#
# element.click()
# time.sleep(5)
#find element by link text
# element = driver.find_element('link text', 'element_link_text')
# driver.get('https://omayo.blogspot.com/')
# element = driver.find_element('link text', 'Page One')
# element.click()
# time.sleep(5)

#find element by partial link text
# element = driver.find_element('partial link text', 'element_partial_link_text')
# driver.get('https://omayo.blogspot.com/')
# element = driver.find_element('partial link text', 'Page')
# element.click()
# time.sleep(5)

#find element by tag name
# element = driver.find_element('tag name', 'element_tag_name')
# driver.get('https://omayo.blogspot.com/')
# print(driver.find_element('tag name', 'h1').text)
# time.sleep(5)

#find element by class name
# element = driver.find_element('class name', 'element_class_name')
# driver.get('https://omayo.blogspot.com/')
# element = driver.find_element('class name', 'date-header')
# print(element.text)
# time.sleep(5)
#find element by css selector
# element = driver.find_element('css selector', 'element_css_selector')
# driver.get('https://omayo.blogspot.com/')
# element = driver.find_element('css selector', 'h2.date-header')
# print(element.text)
# time.sleep(5)

#find element by tag name
# element = driver.find_element('tag name', 'element_tag_name')



#find element by attribute
# element = driver.find_element('attribute', 'element_attribute')

#get attribute
# element.get_attribute('attribute')


#send keys
# element.send_keys('keys')

#click
# element.click()

#clear
# element.clear()

#quit
# driver.quit()

#close
# driver.close()

#maximize window
# driver.maximize_window()

#minimize window
# driver.minimize_window()

#scroll
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#back
# driver.back()

#forward
# driver.forward()

#shortcuts
# from selenium.webdriver.common.keys import Keys
# element.send_keys(Keys.RETURN)
# element.send_keys(Keys.TAB)
# element.send_keys(Keys.ESCAPE)
# element.send_keys(Keys.F1)
# element.send_keys(Keys.F2)


#example
# driver.get('https://omayo.blogspot.com/')
# element = driver.find_element('id', 'multiselect1')
# for i in element.find_elements('tag name', 'option'):
#     if i.text == 'Volvo':
#         i.click()
#         time.sleep(1)
#

# #example
# driver.get('https://omayo.blogspot.com/')
# element = driver.find_element('name', 'login')
# element.find_element('name', 'userid').send_keys('admin')
# element.find_element('name', 'pswrd').send_keys('admin')
# # element.find_element('value', 'Login').click()
# time.sleep(5)

#
# driver.get('https://in.indeed.com/')
# element = driver.find_element('name', 'q')
# element.send_keys('python')
# time.sleep(3)
# list_name = driver.find_element('id', 'what-autocomplete-suggestions')
# print(list_name.text)
# for i in list_name.find_elements('css selector', 'div.div'):
#     print(i.text)
#
#
#
#
#
# element = driver.find_element('name', 'l')
# element.send_keys('hyderabad')
# time.sleep(5)
# element = driver.find_element('css selector', 'button.yosegi-InlineWhatWhere-primaryButton')
# element.click()
# time.sleep(5)
