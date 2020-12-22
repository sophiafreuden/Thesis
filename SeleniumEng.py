# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:40:37 2020

@author: sof565
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math
from bs4 import BeautifulSoup
import requests

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.rt.com/")

time.sleep(1)

search = driver.find_element_by_name("q")

time.sleep(1)

search.send_keys("soros putin")

time.sleep(1)

search.send_keys(Keys.RETURN)

time.sleep(1)

resultsno = driver.find_element_by_class_name("search-serp__total").text

resultsno = resultsno[:-8]

resultsno = int(resultsno)

def clicker(number):
    clicked = 0
    rawpages = number / 10
    pages = math.ceil(rawpages)
    clicks = pages - 1
    while clicked < clicks:
        time.sleep(1)
        element = driver.find_element_by_link_text("More")
        time.sleep(1)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        if clicked > clicks:
            break
        clicked += 1
    
clicker(resultsno)

time.sleep(1)

rawlinks = []

for a in driver.find_elements_by_xpath('.//a[@class="link link_hover"]'):
    rawlinks.append(a.get_attribute('href'))

links = []

for link in rawlinks:
    if link not in links:
        links.append(link)
        
for link in links:
    print(link)
    
print("This search has pulled " + str(len(links)) + " links.")

rt1 = requests.get(links[1])

page = BeautifulSoup(rt1.content, "html.parser")

rawtext = page.find_all("p")

text = rawtext[0:-5]

paras = []

for p in text:
    paras.append(p.get_text())
    
print(paras)

# This works as is, but the example article that I have it print contains strange
# mark up characters as well as Tweets that have been embedded into the article.
# I will have to figure out a way around these things, as well as add article
# meta data and put it all into a nice CSV file.









