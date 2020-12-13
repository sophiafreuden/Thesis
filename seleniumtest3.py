# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:37:12 2020

@author: sof565
"""
#  THIS IS A CLONE OF MY SECOND SELENIUM TEST SCRIPT. This one is to continue
# to show how selenium works. Refer to seleniumtest.py for initial steps.
# This script is specifically for the last part of the second video in the
# YouTube tutorial on selenium. See bit.ly link below for help.

# NOTE FOR SCRIPT 3: I've stripped a lot of my commentary that was originally
# in 1 and 2 to make this script shorter and easier to read. Refer to those
# scripts if you get confused about what certain elements do. The new elements
# here should have proper commentary.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys #note uppercase K

# The following packages are from the selenium documentation online.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# If no errors pop up in the console with import selenium, then this is
# working! If you're not sure how to get selenium installed on your
# computer, try:
# https://bit.ly/3m58mo9
# This is a great YouTube tutorial series on selenium, which includes
# installation and some debugging solutions.

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

print(driver.title) 
search = driver.find_element_by_name("s")

search.send_keys("test")

search.send_keys(Keys.RETURN)

# The try and except below are copied from the the selenium documentation
# online, which you can find here: https://selenium-python.readthedocs.io/waits.html
# Make sure you load the appropriate packages above.

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("article")
    # Note "s" in elements above!!
    # This will look for all elements that have the tag name article and put them
    # in a list. The for loop below is for iterating through that list, finding
    # the headers specifically, and printing those headers. Think of it like
    # going down a tag family from parent to child and then selecting the desired
    # elements. I recommend doing courses/tutorials on HTML, Python, and Beautiful-
    # Soup if any of this is confusing or the jargon doesn't make sense. 
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        # Make sure the entry-summary above has a dash, not an underscore.
        # The video originally had entry-title, but that doesn't work and the
        # video host fixes it in the video.
        print(header.text)
    time.sleep(5)

finally:
    driver.quit()

# The above code should work and spit out a bunch of paragraphs taken from the
# webpage below. I will do the third video in a fourth test script.