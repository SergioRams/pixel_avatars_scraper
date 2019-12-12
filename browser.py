from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ChromeBrowser:

    def __init__(self, page):
        # Google chrome setup
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path='drivers/chromedriver', chrome_options=chrome_options)
        self.driver.maximize_window()
        self.driver.get(page)

    def close(self):
        self.driver.quit()


class FirefoxBrowser:
    """ not tested yet """
    pass
