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
import pandas as pd
import re

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

rt1 = requests.get(links[0])

page = BeautifulSoup(rt1.content, "html.parser")

# The code and comments in lines 84-110 are for extracting paragraph text.
# The code for after is for extracting title and date.

rawtext = page.find_all("p")

text = rawtext[0:-5]

paras = []

for p in text:
    paras.append(p.get_text())

def concatenator(list):
    temp = ""
    for element in list:
        temp += (element + " ")
    return temp

alltext = concatenator(paras)

print(alltext)

# I have decided to keep the Tweets to be consistent with my chapter on Hungary
# and I don't think there's a good solution to the issue of strange HTML characters,
# though I'm not seeing any in the test article I've done. I'm wondering if
# concatenating the strings somehow gets rid of them, though that seems highly
# unlikely.

# So I later tested this on the last link available that was scraped (index 92),
# which dates to 2009. It worked (huzzah) and also didn't print any weird HTML
# characters. Call it witchcraft, call it some kind of poorly understood coding
# fluke, but it's not transcribing those characters here.

# Next step will be figuring out how to scrape multiple articles plus their
# meta data and put that all into a CSV file.

rawdate = page.find(attrs = {'class': 'date date_article-header'})

# The strip argument below strips the texts of the extra white space they
# may come with.

date = rawdate.get_text(strip = True)

print(date)

rawtitle = page.find(attrs = {'class': 'article__heading'})

title = rawtitle.get_text(strip = True)

print(title)

# Time to put this into a test CSV file.

# The line below will create an empty data frame.

df = pd.DataFrame()

# Below I will put the content, title, and date into lists, and then put
# those lists as columns in the pandas data frame. I don't need to add
# the links to a list because "links" is already in list format.

titles = []

titles.append(title)

alltexts = []

alltexts.append(alltext)

dates = []

dates.append(date)

linkstemp = []

linkstemp.append(links[0])

df["URLS"] = linkstemp
df["title"] = titles
df["content"] = alltexts
df["date"] = dates

# print(df)
# This prints kinda funny, but I think it's working. I will save it as a CSV
# file to investigate if it exports well.

df.to_csv("test.csv", sep='*', index=False)

# This importing works, sort of. Opening it in excel reveal a bunch of formating
# problems, but it does produce a CSV file with the data....




