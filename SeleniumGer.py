# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 17:02:55 2021

@author: sof565
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import math
from bs4 import BeautifulSoup
import requests
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://de.rt.com/")

button1 = driver.find_elements_by_xpath('.//a[@class="SearchForm-headerBtn"]')

button1[0].click()

time.sleep(1)

search = driver.find_elements_by_xpath('.//input[@class="Input-root Input-hasIconRight Input-size_l Input-fill_grey "]')
# For whatever reason, the search element above won't work if you use name.

# Change the search term below as needed.
search[0].send_keys("apfel")

time.sleep(1)

dt = driver.find_elements_by_xpath('.//input[@name="dt"]')

time.sleep(1)

dt[0].send_keys("31-12-2019")

time.sleep(1)

search[0].send_keys(Keys.RETURN)

time.sleep(2)

# This is seemingly working up to this point...

# With search results roughly at or below 500, the "Weiter" button will pull
# an initial 10 results plus 10 more per click. This changes if you ping a
# ridiculously high number of results. To see what I mean, search "merkel"
# with no date restrictions and try clicking "Weiter."

results = driver.find_element_by_xpath('.//p[@class="SearchForm-total Text-type_6 ColorTxt-LightGrey"]').text

resultsno = int(results[:-15])

print("You have pinged " + str(resultsno) + " results.")

if resultsno >= 500:
    print("Many results. Try narrowing your search as the clicker function may not work.")

if resultsno == 0:
    print("No results found. Chrome will close automatically and this script will halt.")
    driver.quit()
    sys.exit()

time.sleep(1)

def clicker(number):
    clicked = 0
    rawpages = number / 10
    pages = math.ceil(rawpages)
    print("Pages is " + str(pages) + ".")
    clicks = pages - 1
    print("Clicks is " + str(clicks) + ".")
    while clicked < clicks:
        time.sleep(3) # Usually 3, more if "Weiter" button disappears in console
        button = driver.find_element_by_xpath('.//button[@class="Button-root Button-is1to1 Button-type_l Button_dark"]')
        time.sleep(3) # Usually 3, more if "Weiter" button disappears in console
        driver.execute_script("arguments[0].click();", button)
        if clicked > clicks:
            break
        clicked += 1
        print("Pages clicked = " + str(clicked) + ".")
    print("Clicking completed successfully.")

if resultsno > 10:
    print("Enough results to click through.")
    clicker(resultsno)

if resultsno <= 10 and resultsno != 0:
    print("10 or fewer results. No clicking necessary.")

time.sleep(1)

# "Link-root Link-isFullCard "

links = []

for a in driver.find_elements_by_xpath('.//a[@class="Link-root Link-isFullCard "]'):
    links.append(a.get_attribute('href'))

time.sleep(1)

# It seems that the html class used here also pulls the "Top-Artikel" links,
# which are typically not relevant to the search results. I've tried a variety
# of search terms, all of which pull different numbers of search results. In
# each instance, the "Top-Artikel" links are always at the end of the links list.
# For this reason, I will cut off the last five results, but it's best to be aware
# of this phenomenon.

links = links[:-5]

for link in links:
    print(link)

print("This search has pulled a revised " + str(len(links)) + " links.")

def concatenator(list):
    temp = ""
    for element in list:
        temp += (element + " ")
    return temp

df = pd.DataFrame()

dates = []
titles = []
alltexts = []
all_links = []

counter = 0

print("Beginning article scrape.")



