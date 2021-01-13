# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:37:12 2020

@author: sof565
"""
#  This is an extension of my original nine scripts. This one is to show how
# to do stuff in RT Russian. Refer to seleniumtests 1-9 for initial steps.

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
import sys
import math
from bs4 import BeautifulSoup
import requests
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

# Change the URL below to what you need it to be.

driver.get("https://russian.rt.com/search?q=%D0%B0%D0%BF%D0%B5%D0%BB%D1%8C%D1%81%D0%B8%D0%BD+%D1%84%D1%80%D1%83%D0%BA%D1%82&type=&df=&dt=2019-12-31")

closepopup = driver.find_elements_by_xpath('.//a[@class="subscribe__close js-subscribe-close"]')

time.sleep(1)

closepopup[0].click()

time.sleep(1)

results = driver.find_element_by_xpath('.//p[@class="search-serp__total"]').text

resultsno = int(results[-3:])

print("You have pinged " + str(resultsno) + " results.")

if resultsno >= 300:
    print("Too many results. Try narrowing your search.")
    driver.quit()
    sys.exit()

if resultsno == 0:
    print("No results found. Chrome will close automatically and this script will halt.")
    driver.quit()
    sys.exit()

def clicker(number):
    clicked = 0
    rawpages = number / 15
    pages = math.ceil(rawpages)
    print("Pages is " + str(pages) + ".")
    clicks = pages - 1
    print("Clicks is " + str(clicks) + ".")
    while clicked < clicks:
        time.sleep(3) # Usually 3, more if "More" button disappears in console
        button = driver.find_element_by_xpath('.//a[@class="button__item button__item_listing"]')
        time.sleep(3) # Usually 3, more if "More" button disappears in console
        driver.execute_script("arguments[0].click();", button)
        if clicked > clicks:
            break
        clicked += 1
        print("Pages clicked = " + str(clicked) + ".")
    print("Clicking completed successfully.")

if resultsno > 15:
    print("Enough results to click through.")
    clicker(resultsno)

if resultsno <= 15 and resultsno != 0:
    print("10 or fewer results. No clicking necessary.")

time.sleep(1)

links = []

for a in driver.find_elements_by_xpath('.//a[@class="link link_color"]'):
    links.append(a.get_attribute('href'))

time.sleep(1)

for link in links:
    print(link)

print(len(links))

# driver.quit()

