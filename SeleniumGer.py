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

time.sleep(3)

search = driver.find_elements_by_xpath('.//input[@class="Input-root Input-hasIconRight Input-size_l Input-fill_grey "]')
# For whatever reason, the search element above won't work if you use name.

search[0].send_keys("soros")

time.sleep(1)

dt = driver.find_elements_by_xpath('.//input[@name="dt"]')

time.sleep(1)

dt[0].send_keys("31-12-2019")

time.sleep(3)

search[0].send_keys(Keys.RETURN)

# This is seemingly working up to this point...

# With search results roughly at or below 500, the "Weiter" button will pull
# an initial 10 results plus 10 more per click. This changes if you ping a
# ridiculously high number of results. To see what I mean, search "merkel"
# with no date restrictions and try clicking "Weiter."



