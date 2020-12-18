# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:40:37 2020

@author: sof565
"""

# See test scripts 1-4 for set up and basic commands.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.rt.com/")

link = driver.find_element_by_link_text("Pentagon lost track of over HALF of ‘sensitive’ equipment provided to Afghanistan’s military – watchdog")

# It took a little messing around to figure out. RT links often have a lot of
# space in their text fields. Just copy the plain text without the space on
# either end and put it in the find_element_by_link text.

time.sleep(2)

link.click()

time.sleep(2)

driver.quit()

# In the next script, I will attempt to search for a term that has at least
# two pages of results, click the "more" button, and scrape the links to
# the articles.


