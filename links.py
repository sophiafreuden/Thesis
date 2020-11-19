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

for link in soup.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])