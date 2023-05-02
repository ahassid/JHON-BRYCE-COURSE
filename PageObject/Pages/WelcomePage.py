from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class WelcomePage(object):

    def __init__(self, driver):
        self.driver = driver

    def Welcome(self):
        productsPrices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return productsPrices
