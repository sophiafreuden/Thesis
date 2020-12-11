# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:37:12 2020

@author: sof565
"""

# import selenium

from selenium import webdriver

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

print(driver.title) #This should pring 'Tech with Tim...' in the console and
#  then close the window that it opened. Notice that if you interact with
# the window outside of spyder (i.e. by clicking on it) before you've coded
# a quit/close function, it will keep that window/tab open. I recommend
# playing around with this just to see what things do.

driver.quit()




