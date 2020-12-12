# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:37:12 2020

@author: sof565
"""
#  THIS IS A CLONE OF MY INITIAL SELENIUM TEST SCRIPT. This one is to continue
# to show how selenium works. Refer to seleniumtest.py for initial steps.

# import selenium

# Make sure to import the keys package below for this clone!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys #note uppercase K

# The following packages are from the selenium documentation online.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# We're keeping the time package below the later imports above for now.
import time

# The keys package allows you to hit virual keys (e.g. enter, esc) while
# interacting with webpages with selenium.

# If no errors pop up in the console with import selenium, then this is
# working! If you're not sure how to get selenium installed on your
# computer, try:
# https://bit.ly/3m58mo9
# This is a great YouTube tutorial series on selenium, which includes
# installation and some debugging solutions.

PATH = "C:\Program Files (x86)\chromedriver.exe"

# There might be a little yellow triangle that pops up to the left of import
# selenium/from selenium... before you type driver = ... Don't  worry about
# that.

driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

# This should open a webpage in a new Chrome window. You  might get a pop
# up window from your computer security software about opening a new program
# with Spyder. Make sure to give it proper permission so it can open these
# webpages.

# This particular website is just the website the YouTube tutorial uses. NOTE:
# certain webpages have user agreements or even laws that prevent people from
# scraping. Know what you're getting into before you start messing around.
# Also general scraping etiquette: don't overwhelm a website with requests
# (clicks) so that it crashes. A good rule of thumb is one request/click
# per second.

# driver.close() closes current tab
# driver.quit() closes whole browser window, but not the whole program

# BE CAREFUL ABOUT PARENTHESES WITH BOTH SELENIUM AND BEAUTIFUL SOUP

print(driver.title) #This should pring 'Tech with Tim...' in the console and
#  then close the window that it opened. Notice that if you interact with
# the window outside of spyder (i.e. by clicking on it) before you've coded
# a quit/close function, it will keep that window/tab open. I recommend
# playing around with this just to see what things do.

# Below this line is where this script differs from the original one. See my
# note about the keys package above.

search = driver.find_element_by_name("s")

search.send_keys("test")

search.send_keys(Keys.RETURN)

# Just the above code (plus the sleep and quit commands below) should open
# Chrome at the given website and search the word "test" in page's search bar.
# If it doesn't work, obviously check for typos but also make sure that the
# source code for the page and specifically the search bar hasn't changed.

# print(driver.page_source) this will print the entire page source code (HTML)
# into the console. It's not that helpful, as most of the time digging around
# in the source code on Chrome is more illustrative/useful.

# The try and except below are copied from the the selenium documentation
# online, which you can find here: https://selenium-python.readthedocs.io/waits.html
# Make sure you load the appropriate packages above.

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)
# Don't forget to add the except below otherwise the script will throw an
# error at your next command. ALso make sure your indentations aren't throwing
# errors.
except:
    driver.quit()

# main = driver.find_element_by_id("main") commenting this out with the try
# and except above.
print(main.text)

# time.sleep(5)

# This delays the program by five seconds so it doesn't quit immediately. That
# way we can see what it is we're doing with the commands above.

driver.quit()

# Selenium returns first element that it finds on a page given the parameter
# you've given it. So it's really important to make sure the parameter you're
# using (class, id, name) is unique on that page.

# Everything here should be working. I'm going to clone this script for the
# last part of video #2 in the tutorial series, as my edits are getting
# to convoluted to follow chrologically. If you're getting stuck, go back
# and watch the YouTube videos (1 and 2) on your own.

