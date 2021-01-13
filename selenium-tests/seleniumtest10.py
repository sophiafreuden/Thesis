# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:37:12 2020

@author: sof565
"""
#  This is an extension of my original nine scripts. This one is to show how
# to do stuff in RT Russian. Refer to seleniumtests 1-9 for initial steps.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://russian.rt.com/search?q=%D1%81%D0%BE%D1%80%D0%BE%D1%81")

# driver.close() closes current tab
# driver.quit() closes whole browser window, but not the whole program

# closepopup = driver.find_element_by_class_name(name="subscribe__close js-subscribe-close")

closepopup = driver.find_elements_by_xpath('.//a[@class="subscribe__close js-subscribe-close"]')

# ("subscribe__close js-subscribe-close")

time.sleep(3)

print("working so far")

# For whatever reason, closepopup was being saved a list len 1. So I had to
# index it here.
closepopup[0].click()

print("working so far 2")

dateto = driver.find_element_by_xpath('.//input[@id="input-calendar-dt"]')

print("working so far 3")

time.sleep(3)

dateto.send_keys(Keys.DELETE)

time.sleep(3)

dateto.send_keys("12-31-2019")

time.sleep(3)

dateto.send_keys(Keys.RETURN)

time.sleep(3)

print("working so far 4. driver will quit automatically")

# So while this does "work," for whatever reason the dates box doesn't always
# render the Latin dates vs. the Cyrillic ones. It will work sometimes with
# this code and other times not, even if I haven't changed anything.

# I think the best thing to do is to just pull URLs from RT Russian by hand
# and feed them into the initial driver.get().

# I will do that in a new script (11).

driver.quit()

