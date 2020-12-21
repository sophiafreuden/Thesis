# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:40:37 2020

@author: sof565
"""

# See test scripts 1-6 for set up, basic commands, and initial tests.

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

search.send_keys("mango")

time.sleep(2)

search.send_keys(Keys.RETURN)

time.sleep(2)

click_counter = 0

# Mango is just a random search term that has a few pages of stories on RT.
element = driver.find_element_by_link_text("More")

time.sleep(2)

driver.execute_script("arguments[0].click();", element)

time.sleep(2)

click_counter += 1

element = driver.find_element_by_link_text("More")

time.sleep(2)

driver.execute_script("arguments[0].click();", element)

click_counter += 1

time.sleep(5)

if click_counter == 2:
    driver.quit()

print("Click counter = " + str(click_counter) + ". If it is 2, Chrome will close automatically. Bye bye!")

# The code above is working for me as is. There is likely a more sophisticated
# way of clicking through pages than copying and pasting like how I have here
# This method works if you only need to make a couple clicks, but if you need
# to click a lot, you should probably  write a function that does this for you.

# The next script will focus on pulling links from the pages we've clicked
# through.


