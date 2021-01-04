# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:05:09 2021

@author: sof565
"""

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import sys
# import math
from bs4 import BeautifulSoup
import requests
# import pandas as pd


rt = requests.get("https://www.rt.com/news/511456-assange-extradition-hearing-verdict-announced/")
# https://www.rt.com/uk/311563-girl-12-mensa-iq/
# So I can't get the mensa link above to work regardless of what tag I try
# scraping for. I'm not going to spend more time on it at this point, but
# it seems like some articles just won't get scraped.
page = BeautifulSoup(rt.content, "html.parser")
# First is the text.
rawtext = page.find_all("p")
text = rawtext[0:-4]
paras = []

def concatenator(list):
    temp = ""
    for element in list:
        temp += (element + " ")
    return temp


for p in text:
    paras.append(p.get_text(strip = True))

alltext = concatenator(paras)
print("Paragraphs concantenated.")
print(alltext)










