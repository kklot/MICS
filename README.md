# MICS
automate MICS dataset download

TODO

[ ] Port to an R package
[ ] Checking file hash to ignore dowloadning existing file


# Required libs

```python
import os, urllib
from bs4 import BeautifulSoup
import csv, pandas, re, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
```

# Logging in

This will open a new browser window (Firefox in this case).

Use your username, password, pass the reCaptcha and click login (then make no more movement in the browser please).


```python
browser = webdriver.Firefox()
login_url = "https://mics.unicef.org/visitors/sign-in"
target_url = "https://mics.unicef.org/surveys"
browser.get(login_url)
```

If we run the whole script, the rest of the code will wait until MICS logged in successfully and automatically redirect to surveys site.

```python
def is_login(driver):
    return(driver.current_url == target_url)
WebDriverWait(browser).until(is_login)
```

# Get download urls

```python
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
```

    1
    2
    3
    4
    5
    6

```python
for file in links:
    filename = re.sub('%20', '_', os.path.basename(file))
    tst = urllib.request.urlretrieve(file, filename)
    print('Downloaded'+filename)
```

    DownloadedBangladesh_MICS6_SPSS_Datasets.zip
    DownloadedTurkmenistan_MICS6_SPSS_Datasets.zip
    DownloadedZimbabwe_MICS6_SPSS_Datasets.zip
    DownloadedKiribati_MICS6_Datasets.zip
    DownloadedRepublic_of_North_Macedonia_MICS6_Datasets.zip
    DownloadedRepublic_of_North_Macedonia_%28Roma_Settlements%29_MICS6_Datasets.zip
    ...
