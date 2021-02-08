# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:00:53 2021

@author: sof565
"""

# This is the Prosem script meant to show the basics of Selenium and Beautiful
# Soup in Python.

# The first thing you need to do is install Selenium. I will show you how to do
# that on Zoom. Be sure to follow the instructions in the accompanying PDF.
# There is a lot of text there you can copy and paste.

# Part 1: Loading Selenium and WebDriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Make sure quotation marks are straight! If curly, re-type by hand.
# PC:
PATH = "C:\Program Files (x86)\chromedriver.exe"
# Mac:
# PATH = "/Applications/chromedriver.exe"

driver = webdriver.Chrome(PATH)

# Part 2: Opening Chrome

driver.get("https://www.rt.com/")

# Part 3: Using the Search Field

search = driver.find_element_by_name("q")

# Now add Keys and time packages.

# Delay by two seconds.
time.sleep(2)

# Type "soros russia" into search field.
search.send_keys("soros russia")

time.sleep(2)

# Hit enter.
search.send_keys(Keys.RETURN)

# Part 4: Clicking

# This tells Selenium to find and click the "More" button at the bottom of the
# RT search results page.

element = driver.find_element_by_link_text("More")

time.sleep(1)

driver.execute_script("arguments[0].click();", element)










