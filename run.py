#!/usr/bin/env python3
# coding: utf-8
# 
# See github.com/kklot/MICS
# 
# 

import os, urllib, re, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def is_login(driver):
    return(driver.current_url == target_url)

# # Logging in
# 
# This will open a new browser window (Firefox in this case).
# 
# Use your username, password, pass the reCaptcha and click login (then make no more movement in the browser).

browser = webdriver.Firefox()
login_url = "https://mics.unicef.org/visitors/sign-in"
browser.get(login_url)

# some waiting function (after login the MICS automatically redirect to surveys site)
target_url = "https://mics.unicef.org/surveys"
WebDriverWait(browser).until(is_login)


# # Get download urls

morepage = True
page_index = 1
links = []
while morepage:
    print(page_index)
    papa = browser.find_element_by_css_selector("#pages .pagination li:last-child")
    meme = browser.find_element_by_css_selector("#pages .pagination li:last-child a")
    index_i = BeautifulSoup(browser.page_source)
    for row in index_i.find_all('div', 'dataset-cell'):
        for link in row.find_all('a'):
            dll = link.get('href')
            if (dll != None):
                links.append(dll)
    lastpage = bool(re.search(r'disabled', papa.get_attribute('class')))
    morepage = not lastpage
    if (morepage):
        meme.click()
    page_index += 1
    time.sleep(5)

# # Download files to current folder
# 
# see todo list: github.com/kklot/MICS
# 
for file in links:
    filename = re.sub('%20', '_', os.path.basename(file))
    tst = urllib.request.urlretrieve(file, filename)
    print('Downloaded '+filename)
