# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:40:37 2020

@author: sof565
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.rt.com/")

time.sleep(2)

search = driver.find_element_by_name("q")

time.sleep(1)

search.send_keys("soros romania")

time.sleep(1)

search.send_keys(Keys.RETURN)

time.sleep(1)

element = driver.find_element_by_link_text("More")

time.sleep(1)

driver.execute_script("arguments[0].click();", element)

time.sleep(1)

links = []

for a in driver.find_elements_by_xpath('.//a[@class="link link_hover"]'):
    links.append(a.get_attribute('href'))

links2 = []

for link in links:
    print(link)
    if link not in links2:
        links2.append(link)
        
for link in links2:
    print(link)
    
# Huzzah!

# This is the last of the seleniumtest script series. The next script I make
# will be my formal scraper in selenium.





