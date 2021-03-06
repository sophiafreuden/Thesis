# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:40:37 2020

@author: sof565
"""

# See test scripts 1-7 for set up, basic commands, and initial tests.
# This script attempts to figure out how to pull links from pages with Selenium.
# While progress is made here, see script 9 for a better version.

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

time.sleep(2)

search.send_keys("soros romania")

time.sleep(2)

search.send_keys(Keys.RETURN)

time.sleep(2)

element = driver.find_element_by_link_text("More")

time.sleep(2)

driver.execute_script("arguments[0].click();", element)

time.sleep(2)

links = []

for a in driver.find_elements_by_xpath('.//a'):
    links.append(a.get_attribute('href'))

for link in links:
    print(link)
    
# selec_links = driver.find_element_by_partial_link_text('/news/')
# I think this is for the actual text of the link, not the href text.

# See seleniumtest9 for a version that figures this issue out.





