# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 20:23:41 2021

@author: sof565
"""

# This is the Prosem script meant to show the basics of content scraping with
# BeautifulSoup in Python.
# See the first script in this series for using Selenium in Python.

# Part 1: Loading BeautifulSoup and requests
from bs4 import BeautifulSoup
import requests

# Part 2: Get HTML from test article

rt = requests.get("https://www.rt.com/op-ed/514770-time-electiion-fortified-color-revolution/")
page = BeautifulSoup(rt.content, "html.parser")

# Part 3: Create titles list

titles = []

# Part 4: Scrape the title

rawtitle = page.find(attrs = {'class': 'article__heading'})

title = rawtitle.get_text(strip = True)

titles.append(title)

print(titles)

# Part 5: Create dates list
dates = []

# Part 6: Scrape the date

rawdate = page.find(attrs = {'class': 'date date_article-header'})

date = rawdate.get_text(strip = True)

dates.append(date)

print(dates)

# Part 7: Create paragraphs list
paragraphs = []

# Part 8: Scrape the paragraphs

text = page.find_all("p")

for p in text:
    paragraphs.append(p.get_text(strip = True))
    
for paragraph in paragraphs:
    print(paragraph)

# All done!

