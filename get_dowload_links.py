def get_dowload_links(versions = [], sleep=5, browser=browser):
    # if no version is provided, we download all, if a list we match and extract matched
    to_download = ["MICS"+str(i) for i in range(2,7)] # 2020
    if versions:
        to_download = list(set(versions), set(to_download))
    morepage = True
    page_index = 1
    links = []
    while morepage:
        time.sleep(sleep) # slow loading MICS
        
        try:
            popup = browser.find_element_by_xpath("//div[contains(@class, 'survey_invite_container')]")
            if length(popup) > 0:
                browser.find_elements_by_css_selector('[aria-label="Close"]').click()
            # browser.execute_script("arguments[0].style.visibility='hidden'", popup)
            print("There was a pop up but I closed it!")
        except NoSuchElementException:
            pass
        
        print("Processing page "+str(page_index))
        
        papa = browser.find_element_by_css_selector("#pages .pagination li:last-child")
        meme = browser.find_element_by_css_selector("#pages .pagination li:last-child a")
        
        index_i = BeautifulSoup(browser.page_source)
        for row in index_i.find_all('div', 'dataset-cell'):
            for link in row.find_all('a'):
                dll = link.get('href')
                if (dll != None):
                    # when there is available dataset to download, get unique version
                    link_version = re.findall('MICS\d', urllib.parse.unquote(dll)) # be duplicates
                    if link_version[0] in to_download:
                        links.append(dll)

        lastpage = bool(re.search(r'disabled', papa.get_attribute('class')))
        morepage = not lastpage
        if (morepage):
            meme.click()
        page_index += 1
    print("There are "+str(len(links))+" file(s) detected.")
    return links
