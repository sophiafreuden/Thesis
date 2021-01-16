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

# Change the URL below to what you need it to be re: search term and date.

driver.get("https://russian.rt.com/search?q=%D0%BA%D0%BB%D0%B8%D0%BD%D1%82%D0%BE%D0%BD+%D0%BC%D0%B0%D0%B9%D0%B4%D0%B0%D0%BD&type=&df=&dt=2019-12-31")

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

print("This search has pulled " + str(len(links)) + " links.")

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

for link in links:
    print("Link is at links index " + str(counter) + ".")
    rt = requests.get(link)
    page = BeautifulSoup(rt.content, "html.parser")
    paras = []
    rawsummary = page.find('div', attrs = {'class': 'article__summary article__summary_article-page js-mediator-article'})
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
        rawdate = page.find(attrs = {'class': 'date'})
        if rawdate == None :
            print("This date will be skipped.")
            date = "Skipped"
            dates.append(date)
            rawtitle = page.find(attrs = {'class': 'article__heading article__heading_article-page'})
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
        date = newdate[:-6]
        dates.append(date)
        rawtitle = page.find(attrs = {'class': 'article__heading article__heading_article-page'})
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
    # Index range below optional. Some articles include extra p that if cut
    # off also cut paragraphs in older articles off. Try -5 if using for 
    # different results.
    text = rawtext # [0:-4]
    for p in text:
        paras.append(p.get_text(strip = True))
    alltext = concatenator(paras)
    alltexts.append(alltext)
    rawdate = page.find(attrs = {'class': 'date'})
    if rawdate == None :
        print("This date will be skipped.")
        date = "Skipped"
        dates.append(date)
        rawtitle = page.find(attrs = {'class': 'article__heading article__heading_article-page'})
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
    date = newdate[:-7]
    dates.append(date)
    rawtitle = page.find(attrs = {'class': 'article__heading article__heading_article-page'})
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

# I notice one title was skipped in my test for this. It was because video
# articles have their titles under a different tag/class. These pages typically
# only have a paragraph or so of text, so I'm not inclined to change anything.

if counter == resultsno:
    print("Article scraping done.")

df["date"] = dates
df["title"] = titles
df["content"] = alltexts
df["URL"] = all_links

print(df)

df.to_csv("RT_rus.txt", sep='*', index=False)
# After doing some digging, it seems saving a CSV with Cyrillic is a bad
# idea. This will save it as a txt file that you can then read into r with
# read.delim() or read.delim2(). I won't have any easy way of editing out
# the rows with video articles, but if these get read into R, that's not a
# big deal.

print(" ")
print("Export complete. Chrome will close automatically. Bye bye!")

# Be sure to rename your txt files immediately. I will follow a phonetic
# spelling of the Russian searches in Latin letters.

# Will have to find/replace all the date months with numbers in notepad
# until I figure out how to extract the datetime from the HTML.

time.sleep(3)

driver.quit()

