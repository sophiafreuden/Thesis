# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:05:08 2020

@author: sof565
"""

from bs4 import BeautifulSoup
import requests

rt1 = requests.get("https://www.rt.com/usa/471880-soros-enemies-dictators-lobbying-china/")

page = BeautifulSoup(rt1.content, "html.parser")

text = page.find_all("p")

text2 = text[0:-5]

lst = []

for p in text2:
    lst.append(p.get_text())

