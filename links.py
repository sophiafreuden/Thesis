# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:53:46 2020

@author: sof565
"""

from bs4 import BeautifulSoup
import requests
# import re

raw = requests.get("https://www.rt.com/search?q=russia+soros")

soup = BeautifulSoup(raw.content, "html.parser")

all_links = []

for link in soup.findAll("a"):
    if 'href' in link.attrs:
        all_links.append(link.get('href'))

# print(all_links)

temp = []

for link in soup.find_all("a", attrs={"class": "link link_hover"}):
    if 'href' in link.attrs:
        temp.append(link.get('href'))
    
# print(temp)

temp2 = []

for link in temp:
    if link not in temp2:
        temp2.append(link)
        
print(temp2)

# Brilliant! Next stop is installing and using Selenium for some button
# clicking.
