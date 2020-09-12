import os, urllib
from bs4 import BeautifulSoup
import csv, pandas, re, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

def is_login(driver):
    return(driver.current_url == target_url)
