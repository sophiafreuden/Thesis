# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:40:37 2020

@author: sof565
"""

# This is a fail-safe script meant as a backup in case SeleniumEng doesn't
# work and the past repo isn't accessible on github. This script is functional,
# but messy. I will not make further edits to it.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math
from bs4 import BeautifulSoup
import requests
import pandas as pd
# import re

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

resultsno = driver.find_element_by_class_name("search-serp__total").text

time.sleep(2)

resultsno = resultsno[:-8]

time.sleep(1)

resultsno = int(resultsno)

print("You've pinged " + str(resultsno) + " search results.")

def clicker(number):
    clicked = 0
    rawpages = number / 10
    pages = math.ceil(rawpages)
    print("Pages is " + str(pages) + ".")
    clicks = pages - 1
    print("Clicks is " + str(clicks) + ".")
    while clicked < clicks:
        time.sleep(3)
        element = driver.find_element_by_link_text("More")
        time.sleep(3)
        driver.execute_script("arguments[0].click();", element)
        # time.sleep(3)
        if clicked > clicks:
            break
        clicked += 1
    print("Clicking completed successfully.")
    
# So sometimes I get an issue with the clicker where it says "NoSuchElementException:
# no such element: Unable to locate element". I made the clicker run a little slower
# because it started doing this randomly without me changing the code in the clicker
# or anything before it. I suspect the "More" button just wasn't loading fast
# enough. I've tested this code many times at this point with search terms of varying
# quantity results.

if resultsno > 10:
    print("Enough results to click through.")
    clicker(resultsno)

if resultsno <= 10 and resultsno != 0:
    print("10 or fewer results. No clicking necessary.")
    
if resultsno == 0:
    print("No results found.")

time.sleep(1)

rawlinks = []

for a in driver.find_elements_by_xpath('.//a[@class="link link_hover"]'):
    rawlinks.append(a.get_attribute('href'))

links = []

for link in rawlinks:
    if link not in links:
        links.append(link)
        
# for link in links:
#     print(link)
    
print("This search has pulled " + str(len(links)) + " links.")

def concatenator(list):
    temp = ""
    for element in list:
        temp += (element + " ")
    return temp

df = pd.DataFrame()

titles = []

alltexts = []

dates = []

all_links = []

# print(titles)
# print(all_links)
# print(alltexts)
# print(dates)

counter = 0

for link in links:
    rt = requests.get(link)
    page = BeautifulSoup(rt.content, "html.parser")
    # First is the text.
    rawtext = page.find_all("p")
    text = rawtext[0:-5]
    paras = []
    for p in text:
        paras.append(p.get_text(strip = True))
    alltext = concatenator(paras)
    print("Paragraphs concantenated.")
    alltexts.append(alltext)
    # Next is the date.
    rawdate = page.find(attrs = {'class': 'date date_article-header'})
    date = rawdate.get_text(strip = True)
    dates.append(date)
    # Next is the title.
    rawtitle = page.find(attrs = {'class': 'article__heading'})
    title = rawtitle.get_text(strip = True)
    titles.append(title)
    # Lastly, the URL.
    all_links.append(link)
    counter += 1
    time.sleep(1)
    if counter == len(links):
        print("Loop done.")
        break

print("If " + str(counter) + " equals " + str(len(links)) + ", then loop is done.")

# print(titles)
# print(all_links)
# print(alltexts)
# print(dates)

df["date"] = dates
df["title"] = titles
df["content"] = alltexts
df["URLS"] = all_links

print(df)

df.to_csv("test5.csv", sep=',', encoding='utf-8', index=False)

print("Export complete. Chrome will close automatically. Bye bye!")

time.sleep(3)

driver.quit()

# rt1 = requests.get(links[0])

# page = BeautifulSoup(rt1.content, "html.parser")

# The code and comments in lines 84-110 are for extracting paragraph text.
# The code for after is for extracting title and date.

# rawtext = page.find_all("p")

# text = rawtext[0:-5]

# paras = []

# for p in text:
#     paras.append(p.get_text())

# print("Raw paras:")
# print(paras)

# def concatenator(list):
#     temp = ""
#     for element in list:
#         temp += (element + " ")
#     return temp

# alltext = concatenator(paras)

# print("Concatenated paras:")
# print(alltext)

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

# Upon exporting the pd data frame as a CSV file, I'm seeing weird characters
# where apostrophes should be, for example. I'll try to figure this out at
# a later date. Right now I want to focus on putting the full text scraper
# together.

# rawdate = page.find(attrs = {'class': 'date date_article-header'})

# The strip argument below strips the texts of the extra white space they
# may come with.

# date = rawdate.get_text(strip = True)

# print(date)

# rawtitle = page.find(attrs = {'class': 'article__heading'})

# title = rawtitle.get_text(strip = True)

# print(title)

# Time to put this into a test CSV file.

# The line below will create an empty data frame.

# df = pd.DataFrame()

# Below I will put the content, title, and date into lists, and then put
# those lists as columns in the pandas data frame. I don't need to add
# the links to a list because "links" is already in list format.

# titles = []

# titles.append(title)

# alltexts = []

# alltexts.append(alltext)

# dates = []

# dates.append(date)

# linkstemp = []

# linkstemp.append(links[0])

# print(titles)
# print(linkstemp)
# print(alltexts)
# print(dates)

# df["URLS"] = all_links
# df["title"] = titles
# df["content"] = alltexts
# df["date"] = dates

# print(df)
# This prints kinda funny, but I think it's working. I will save it as a CSV
# file to investigate if it exports well.

# # df.to_csv("test.csv", sep='*', index=False)

# df.to_csv("test4.csv", sep=',', encoding='utf-8', index=False)

# The csv saving function above seems to be the winner. I'm having an internal
# debate about whether I want to format the date pulled from the article
# to no longer include the time. I will come back to this after I finish
# putting the full text scraper together.

# print("Test done.")

# This importing works, sort of. Opening it in excel reveal a bunch of formating
# problems, but it does produce a CSV file with the data....




