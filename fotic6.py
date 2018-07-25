import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir="+r"C:/Users/Administrator/AppData/Local/Google/Chrome/User Data")
browser = webdriver.Chrome(chrome_options=options)
browser.get('http://10.7.101.52:9081/contract/reminiscenceLogin.html#')

browser.find_element_by_name("user.userPassword").send_keys("0")
browser.find_element_by_name("Submit").click()
