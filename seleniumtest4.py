# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:37:12 2020

@author: sof565
"""
#  THIS IS A FOLLOW UP TO MY THIRD SELENIUM TEST SCRIPT. This one is to continue
# to show how selenium works. Refer to seleniumtest.py for initial steps.
# THIS IS NOT A CLONE. This script covers different/new material.
# This script is specifically for the third YouTube tutorial video. See bit.ly
# link below for help.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys #note uppercase K
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# See scripts 1-3 for this code and for the third, fourth, and fifth packages
# above.
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

link = driver.find_element_by_link_text("Python Programming")
# .click() appended to your link variable will click on that variable.
link.click()

# Copied from Selenium documentation.
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )#Notice By.LINK_TEXT change above from boilerplate code and string.
    element.click()
    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )# the sow-button... above is the same as is in the video, but this good change.
    # You might need to go digging around in the page source code to find the
    # correct a href and corresponding ID for that if you get an error here.
    element.click()
    # .back() goes back to the previous page once. Copy and paste for as many
    # times as you need, though there is likely a more sophisticated way of
    # programming that if you need to do it (or any other selenium function)
    #  a bunch.
    driver.back()
    driver.back()
    driver.back()
    # driver.forward() is also an option if you want to go forward.
except:
    driver.quit()
    
# Special note from the video: this isn't really relevant for this video/script,
# but if you're interacting with a text field (such as a search bar) and there
# is already text there (either something you've put there or text that might
# be there by default), you can clear it with .clear, so element.clear()

# The code aboe should work as is. If the browser quits, that means you have
# an error somewhere. Check for typos or to see if the source code for this
# webpage has changed.



