# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:40:37 2020

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

# Step 1: Set Up Selenium

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Step 2: Begin Search. You will need to enter your custom search terms in
# search.send_keys() below (line 36).

driver.get("https://www.rt.com/")

# I've programmed a lot of time.sleep() into this script as rt.com is often
# quite slow.

time.sleep(2)

search = driver.find_element_by_name("q")

time.sleep(2)

search.send_keys("soros democratic party")

time.sleep(2)

search.send_keys(Keys.RETURN)

time.sleep(2)

# Step 3: Calculate Results Total and Determine If Clicking is Necessary.

resultsno = driver.find_element_by_class_name("search-serp__total").text

time.sleep(2)

if resultsno == "Results (0)":
    print("No results found. Chrome will close automatically and this script will halt.")
    driver.quit()
    sys.exit()

if resultsno == "More than 300 results":
    print("Too many results to scrape. Try narrowing your search terms.")
    print("Chrome will close automatically and this script will halt.")
    driver.quit()
    sys.exit()

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
        time.sleep(4) # Usually 3, more if "More" button disappears
        element = driver.find_element_by_link_text("More")
        time.sleep(4) # Usually 3, more if "More" button disappears
        driver.execute_script("arguments[0].click();", element)
        if clicked > clicks:
            break
        clicked += 1
        print("Pages clicked = " + str(clicked) + ".")
    print("Clicking completed successfully.")    

if resultsno > 10:
    print("Enough results to click through.")
    clicker(resultsno)  # Should be set to resultsno unless testing smaller/
    # specific number.

if resultsno <= 10 and resultsno != 0:
    print("10 or fewer results. No clicking necessary.")
    
if resultsno == 0:
    print("No results found. Chrome will close automatically and this script will halt.")
    driver.quit()
    exit()

# Step 4: Scrape the Article Links

time.sleep(1)

rawlinks = []

for a in driver.find_elements_by_xpath('.//a[@class="link link_hover"]'):
    rawlinks.append(a.get_attribute('href'))

links = []

for link in rawlinks:
    if link not in links:
        links.append(link)

print("This search has pulled " + str(len(links)) + " links.")

# Step 5: Set Up Empty pd Data Frame and Scrape Article Text and Meta Data

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

# links = links[0:174]

# linkstemp = links[176:295]

# for link in linkstemp:
#     if link not in links:
#         links.append(link)

for link in links:
    print("Link is at links index " + str(counter) + ".")
    rt = requests.get(link)
    page = BeautifulSoup(rt.content, "html.parser")
    paras = []
    rawsummary = page.find('div', attrs = {'class': 'article__summary summary'})
    if rawsummary == None :
        print("No summary in article.")
        rawtext = page.find_all("p")
        # Index range below optional. Some articles include extra p that if
        # cut off also cut paragraphs in older articles off. Try -5 if using
        # for different results.
        text = rawtext # [0:-4]
        for p in text:
            paras.append(p.get_text(strip = True))
        alltext = concatenator(paras)
        alltexts.append(alltext)
        rawdate = page.find(attrs = {'class': 'date date_article-header'})
        if rawdate == None :
            print("This date will be skipped.")
            date = "Skipped"
            dates.append(date)
            rawtitle = page.find(attrs = {'class': 'article__heading'})
            if rawtitle == None :
                print("This title will be skipped.")
                title = "Skipped"
                titles.append(title)
                all_links.append(link)
                counter += 1
                time.sleep(1)
                continue
            title = rawtitle.get_text(strip = True)
            titles.append(title)
            all_links.append(link)
            counter += 1
            time.sleep(1)
            continue
        newdate = rawdate.get_text(strip = True)
        date = newdate[:-6]
        dates.append(date)
        rawtitle = page.find(attrs = {'class': 'article__heading'})
        if rawtitle == None :
            print("This title will be skipped.")
            title = "Skipped"
            titles.append(title)
            all_links.append(link)
            counter += 1
            time.sleep(1)
            continue
        title = rawtitle.get_text(strip = True)
        titles.append(title)
        all_links.append(link)
        counter += 1
        time.sleep(1)
        continue
    summary = rawsummary.get_text(strip = True)
    paras.append(summary)
    rawtext = page.find_all("p")
    # Index range below optional. Some articles include extra p that if cut
    # off also cut paragraphs in older articles off. Try -5 if using for 
    # different results.
    text = rawtext # [0:-4]
    for p in text:
        paras.append(p.get_text(strip = True))
    alltext = concatenator(paras)
    alltexts.append(alltext)
    rawdate = page.find(attrs = {'class': 'date date_article-header'})
    if rawdate == None :
        print("This date will be skipped.")
        date = "Skipped"
        dates.append(date)
        rawtitle = page.find(attrs = {'class': 'article__heading'})
        if rawtitle == None :
            print("This title will be skipped.")
            title = "Skipped"
            titles.append(title)
            all_links.append(link)
            counter += 1
            time.sleep(1)
            continue
        title = rawtitle.get_text(strip = True)
        titles.append(title)
        all_links.append(link)
        counter += 1
        time.sleep(1)
        continue
    newdate = rawdate.get_text(strip = True)
    date = newdate[:-6]
    dates.append(date)
    rawtitle = page.find(attrs = {'class': 'article__heading'})
    if rawtitle == None :
        print("This title will be skipped.")
        title = "Skipped"
        titles.append(title)
        all_links.append(link)
        counter += 1
        time.sleep(1)
        continue
    title = rawtitle.get_text(strip = True)
    titles.append(title)
    all_links.append(link)
    counter += 1
    time.sleep(1)

if counter == resultsno:
    print("Article scraping done.")

# Step 6: Compose pd Data Frame with Scraped Info and Export as CSV File

df["date"] = dates
df["title"] = titles
df["content"] = alltexts
df["URL"] = all_links

print(df)

df.to_csv("RT_eng.csv", sep=',', encoding='utf-8', index=False)

print(" ")
print("Export complete. Chrome will close automatically. Bye bye!")

# Step 7: Close Chrome

time.sleep(3)

driver.quit()

# Some weird HTML characters will appear in the content and title columns in
# the CSV file you export. Use find and replace in Excel to change them into
# what they should be: apostrophes, quotation marks, etc.

# The exported CSV file will be in reverse chronological order (newest at top).
# You will have to manually rename your CSV file for each search you do with
# this script.