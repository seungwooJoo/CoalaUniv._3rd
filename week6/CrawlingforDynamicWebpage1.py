from selenium import webdriver
import time 

driver = webdriver.Chrome('./chromedriver')
driver.get('https://map.naver.com')

driver.find_element_by_css_selector('input#research-input').send_keys('치킨')
driver.find_element_by_css_selector('button.spm').click()
   
for n in range(1,5):
    time.sleep(1)

    stores = driver.find_element_by_css_selector('div.lsnx')
    for store in stores:
        name = store.find_element_by_css_selector('dt > a').text
        addr = store.find_element_by_css_selector('dd.addr').text
        try:    
            phone = store.find_element_by_css_selector('dd.tel').text
        except:
            phone = '전화번호 없음'
        print(name, addr, phone)

    
        page_bar  = driver.find_element_by_css_selector('div.paginate > *')
        page_bar[n+1].click()
driver.close()