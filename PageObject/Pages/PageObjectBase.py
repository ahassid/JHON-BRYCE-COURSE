from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class PageObjectBase:

    def seleniumStart(self, url):
        driver = webdriver.Chrome(
            service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def seleniumEnd(self, driver):
        driver.close()
