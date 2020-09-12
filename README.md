# MICS
automate MICS dataset download

TODO

- [x] Login and download 
- [ ] Port to an R package
- [ ] Checking file hash to ignore dowloading existing file


# Required libs

Using python3

```bash
pip3 install bs4
pip3 install selenium
# and what libs you are still missing...
```

# Logging in

This will open a new browser window (Firefox in this case).

Use your username, password, pass the reCaptcha and click login (then make no more movement in the browser please).
If we run the whole script, the rest of the code will wait until MICS logged in successfully and automatically redirect to surveys site.

```python
def is_login(driver):
    return(driver.current_url == target_url)
WebDriverWait(browser).until(is_login)
```
# Example outputs

Get download urls

```python
    1
    2
    3
    4
    5
    6
```

Dowloading (to current directory)

```python
    DownloadedBangladesh_MICS6_SPSS_Datasets.zip
    DownloadedTurkmenistan_MICS6_SPSS_Datasets.zip
    DownloadedZimbabwe_MICS6_SPSS_Datasets.zip
    DownloadedKiribati_MICS6_Datasets.zip
    DownloadedRepublic_of_North_Macedonia_MICS6_Datasets.zip
    DownloadedRepublic_of_North_Macedonia_%28Roma_Settlements%29_MICS6_Datasets.zip
    ...
```
