from selenium import webdriver
import time 

driver = webdriver.Chrome('./chromedriver')
driver.get('https://map.naver.com')

driver.find_element_by_css_selector('input#research-input').send_keys('치킨')
driver.find_element_by_css_selector('button.spm').click()
time.sleep(0.5)

stores = driver.find_element_by_css_selector('div.lsnx')
for store in stores:
    name = store.find_element_by_css_selector('dt > a').text
    addr = store.find_element_by_css_selector('dd.addr').text
    phone = store.find_element_by_css_selector('dd.tel').text
    print(name, addr, phone)
    
driver.close()