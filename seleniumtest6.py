# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:40:37 2020

@author: sof565
"""

# See test scripts 1-5 for set up, basic commands, and initial test.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.rt.com/")

time.sleep(2)

search = driver.find_element_by_name("q")

time.sleep(2)

search.send_keys("soros romania")

time.sleep(2)

# You probably don't need to add so many timers (and you can shorten yours to
# one second each, I was just trying to be cautious about using RT and not
# getting booted. Some websites will boot Selenium bots and even block IP
# addresses if you get too aggressive with it.)

search.send_keys(Keys.RETURN)

time.sleep(2)

element = driver.find_element_by_link_text("More")

# I initially tried using ...by_class_name() above, but it wasn't working. Try
# different attributes, but make sure those attributes have unique values or
# Selenium won't execute your command.

time.sleep(2)

driver.execute_script("arguments[0].click();", element)

# The code above makes it so you can actually click on the "More" button of
# the RT search results. It's initially covered by another element. This gets
# rid of that element and clicks the proper element (the button) underneath.

time.sleep(2)

driver.quit()

# In the next script, I will attempt to click the "more" button twice on search
# results that have at least three pages.


