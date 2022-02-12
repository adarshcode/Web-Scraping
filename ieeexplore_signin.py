from selenium import webdriver

browser=webdriver.Firefox()

browser.get('https://ieeexplore.ieee.org/Xplore/guesthome.jsp')

buttonelem=browser.find_element_by_link_text('Institutional Sign In')
buttonelem.click()

buttonelem1=browser.find_element_by_link_text('Sign In with Username and Password')
buttonelem1.click()

userelem=browser.find_element_by_name('username')
userelem.send_keys('your_ieeexplore_username')

passelem=browser.find_element_by_name('password')
passelem.send_keys('your_ieeexplore_password')

passelem.submit()