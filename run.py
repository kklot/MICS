import os, urllib
from bs4 import BeautifulSoup
import csv, pandas, re, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from get_dowload_links import get_dowload_links
from download import download


def run_mics(versions = [], overwrite = False, save_to = ".", sleep = 5):
    
    login_url = "https://mics.unicef.org/visitors/sign-in"
    target_url = "https://mics.unicef.org/surveys"
    def is_login(driver):
        return(driver.current_url == target_url)

    browser = webdriver.Firefox()
    browser.get(login_url)
    WebDriverWait(browser,timeout=180).until(is_login) # reCaptcha is hard to solve man
    time.sleep(sleep)
    
    links = get_dowload_links(browser, versions, sleep)
    download(links, overwrite, save_to)
    browser.quit()
    print("Finished!")

run_mics()