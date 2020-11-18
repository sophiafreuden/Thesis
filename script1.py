# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:50:37 2020

@author: sof565
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html.read());
print(bsObj.h1)
print(bsObj.body)

