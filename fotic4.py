from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://10.7.101.52:9081/contract/reminiscenceLogin.html#')
browser.find_element_by_name("user.userCode").send_keys("admin")
browser.find_element_by_name("user.userPassword").send_keys("0")
browser.find_element_by_name("Submit").click()
