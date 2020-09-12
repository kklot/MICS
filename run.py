import "meta.py"
import "get_dowload_links.py"
import "download.py"

def run_mics(versions = [], overwrite = False, save_to = ".", sleep = 5):
    login_url = "https://mics.unicef.org/visitors/sign-in"
    target_url = "https://mics.unicef.org/surveys"
    browser = webdriver.Firefox()
    browser.get(login_url)
    WebDriverWait(browser,timeout=180).until(is_login) # reCaptcha is hard to solve man
    time.sleep(sleep)
    links = get_dowload_links(versions, sleep, browser)
    download(links, overwrite, save_to)
    browser.quit()
    print("Finished!")

run_mics()