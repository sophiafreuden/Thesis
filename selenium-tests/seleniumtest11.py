# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:37:12 2020

@author: sof565
"""
#  This is an extension of my original nine scripts. This one is to show how
# to do stuff in RT Russian. Refer to seleniumtests 1-9 for initial steps.

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
import sys

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://russian.rt.com/search?q=%D1%81%D0%BE%D1%80%D0%BE%D1%81&type=&df=&dt=2019-12-31")

# driver.close() closes current tab
# driver.quit() closes whole browser window, but not the whole program

# closepopup = driver.find_element_by_class_name(name="subscribe__close js-subscribe-close")

closepopup = driver.find_elements_by_xpath('.//a[@class="subscribe__close js-subscribe-close"]')

# ("subscribe__close js-subscribe-close")

time.sleep(3)

print("working so far")

# For whatever reason, closepopup was being saved a list len 1. So I had to
# index it here.
closepopup[0].click()

print("working so far 2")

time.sleep(3)

results = driver.find_element_by_xpath('.//p[@class="search-serp__total"]').text

resultsno = int(results[-3:])

print(resultsno)

if resultsno >= 300:
    print("Too many results. Try narrowing your search.")
    driver.quit()
    sys.exit()

time.sleep(3)

button = driver.find_element_by_xpath('.//a[@class="button__item button__item_listing"]')

print("working so far 3")

time.sleep(3)

driver.execute_script("arguments[0].click();", button)

print("working so far 4")

links = []

for a in driver.find_elements_by_xpath('.//a[@class="link link_color"]'):
    links.append(a.get_attribute('href'))

time.sleep(3)

print(links)

# This is working as is. I think the next script I make will be the full version
# (SeleniumRus).

print("Driver will quit automatically. Bye bye!")

driver.quit()

