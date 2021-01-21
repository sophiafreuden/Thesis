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
search[0].send_keys("orban")

time.sleep(1)

# I have found that sometimes the "Weiter" button stops working in Chrome
# after enough clicks. There's no way to fix this in Python--it's a Chrome/
# internet issue--so I added some lines to select a "date from" in the dates
# search boxes to limit search results. Comment out lines 41-48 as needed.
# dt = driver.find_elements_by_xpath('.//input[@name="df"]')

# time.sleep(1)

# dt[0].send_keys("31-12-2016")

# time.sleep(1)

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
        time.sleep(5) # Usually 5, more if "Weiter" button won't work in Chrome
        button = driver.find_element_by_xpath('.//button[@class="Button-root Button-is1to1 Button-type_l Button_dark"]')
        time.sleep(1) # Usually 1, more if "Weiter" button won't work in Chrome
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

# Because of issues with the "Weiter" button functioning properly, I've included
# this error message and condition. 5 is an arbitrary number; I'm not concerned
# if the scraper doesn't hit every unique link, but it shouldn't be missing
# tons of them. Sometimes the results will have duplicate stories, so len(links)
# won't always equate resultsno.
if (resultsno - len(links)) > 5:
    print("The number of links pulled does not match the number of results.")
    print("Try revising date from search option or sleep time in clicker.")
    print("Chrome will close automatically and this script will halt.")
    print("You can comment out if statement at line 132 to override.")
    driver.quit()
    time.sleep(1)
    sys.exit()

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

# For whatever reason, the extra spaces that appeared at the end of the class
# names in the html were throwing this for loop off and making it impossible
# for it to find the summaries, dates, and titles. I deleted those extra spaces.

for link in links:
    print("Link is at links index " + str(counter) + ".")
    rt = requests.get(link)
    page = BeautifulSoup(rt.content, "html.parser")
    paras = []
    rawsummary = page.find(attrs = {'class': 'Text-root Text-type_1'})
    if rawsummary == None :
        print("No summary in article.")
        rawtext = page.find_all("p")
        text = rawtext
        for p in text:
            paras.append(p.get_text(strip = True))
        alltext = concatenator(paras)
        alltexts.append(alltext)
        rawdate = page.find(attrs = {'class': 'Timestamp-root Timestamp-default'})
        if rawdate == None :
            print("This date will be skipped.")
            date = "Skipped"
            dates.append(date)
            rawtitle = page.find(attrs = {'class': 'HeadLine-root HeadLine-type_2'})
            if rawtitle == None :
                print("Skipped - Title may be under different tag.")
                title = "Skipped - Title may be under different tag."
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
        date = newdate[:-10]
        dates.append(date)
        rawtitle = page.find(attrs = {'class': 'HeadLine-root HeadLine-type_2'})
        if rawtitle == None :
            print("Skipped - Title may be under different tag.")
            title = "Skipped - Title may be under different tag."
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
    text = rawtext
    for p in text:
        paras.append(p.get_text(strip = True))
    alltext = concatenator(paras)
    alltexts.append(alltext)
    rawdate = page.find(attrs = {'class': 'Timestamp-root Timestamp-default'})
    if rawdate == None :
        print("This date will be skipped.")
        date = "Skipped"
        dates.append(date)
        rawtitle = page.find(attrs = {'class': 'HeadLine-root HeadLine-type_2'})
        if rawtitle == None :
            print("Skipped - Title may be under different tag.")
            title = "Skipped - Title may be under different tag."
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
    date = newdate[:-10]
    dates.append(date)
    rawtitle = page.find(attrs = {'class': 'HeadLine-root HeadLine-type_2'})
    if rawtitle == None :
        print("Skipped - Title may be under different tag.")
        title = "Skipped - Title may be under different tag."
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

df["date"] = dates
df["title"] = titles
df["content"] = alltexts
df["URL"] = all_links

print(df)

df.to_csv("RT_ger.txt", sep='*', index=False)

print(" ")
print("Export complete. Chrome will close automatically. Tschüss!")

time.sleep(3)

driver.quit()

# Be sure to rename your txt files immediately. I will follow a non-diacritic
# spelling in the file names of the German searches (i.e. no umlauts, ß = ss).

# See cleanup instructions in the readme.


