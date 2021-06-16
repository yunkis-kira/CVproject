from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver 
#for waiting to load elements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import requests

import time

#configuring Chrome webdriver(previously downloaded)
#from https://sites.google.com/a/chromium.org/chromedriver/downloads
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

page_num = 1

for num in range(page_num):
    the_url = 'https://shopee.vn/%C3%81o-cat.77.1871?page={}'.format(num)
    driver.get(the_url)

    sleep_time = 0.5
    delay = 6
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "shopee__kZMc3xKQ4ab")))
        driver.set_window_size(1500, 768)
        #time.sleep(3)
        print('Page is loaded!')
        #'''
        driver.execute_script("window.scrollTo(0, 250)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 1250)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 1500)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 1750)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 2000)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 2250)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 2500)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 2750)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 3000)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 3250)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 3500)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 3750)")
        time.sleep(sleep_time)
        driver.execute_script("window.scrollTo(0, 4000)")
        time.sleep(sleep_time)
        print('Page is scrolled!')
        #'''
        html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        #print(html)
        soup = BeautifulSoup(html, 'lxml')
        items = soup.find_all('div', class_ = 'col-xs-2-4 shopee-search-item-result__item')
        for item in items:
            item_name = item.find('div', class_ = 'yQmmFK _1POlWt _36CEnF').text
            print('item name:',item_name)
            item_price = item.find('span', class_ = '_29R_un').text.replace('.','')
            print('item price:',item_price,'₫')
            item_sold = item.find('div', class_ = 'go5yPW').text.replace('Đã bán ','')
            item_sold = item_sold.replace(',','.')
            print('items sold:', item_sold)
            item_location = item.find('div', class_ = '_2CWevj').text
            print('item location:', item_location)
            item_img_url = item.find('img', class_ = 'mxM4vG _2GchKS').get('src')
            img_data = requests.get(item_img_url).content
            #Getting rid of special characters in filenames
            img_name = item_name
            img_name = img_name.replace('/','')
            img_name = img_name.replace('\\','')
            img_name = img_name.replace(':','')
            img_name = img_name.replace('*','')
            img_name = img_name.replace('?','')
            img_name = img_name.replace('\"','')
            img_name = img_name.replace('<','')
            img_name = img_name.replace('>','')
            img_name = img_name.replace('|','')
            img_name = "shopee_scraper/img_data/{}.jpg".format(img_name)
            
            
            with open(img_name, 'wb') as handler:
                handler.write(img_data)
            print('')
    except TimeoutException:
        print("Loading took too much time!")

driver.quit()