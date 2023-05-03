import unittest

from selenium.webdriver.chrome import webdriver
from PageObject.Pages.LoginPage import LoginPage
from PageObject.Pages.WelcomePage import WelcomePage
from PageObject.Tests.PageObjectBase import PageObjectBase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class LoginTestPyTest(unittest.TestCase):

    def setUp(self):
        self.base = PageObjectBase()
        self.driver = self.base.seleniumStart('https://www.saucedemo.com/')
        self.loginPage2 = LoginPage(self.driver)
        self.welcomPage2 = WelcomePage(self.driver)

    def testStandardLogin(self):
        self.loginPage2.Login('standard_user', 'secret_sauce')

    def testLockedLogin(self):
        self.loginPage2.Login('locked_out_user', 'secret_sauce')

    def testProblemLogin(self):
        self.loginPage2.Login('problem_user', 'secret_sauce')

    def testPerformanceLogin(self):
        self.loginPage2.Login('performance_glitch_user', 'secret_sauce')

    def testVerifyLogin(self):
        self.loginPage2.Login('standard_user', 'secret_sauce')
        self.welcomPage2.verifyTitle()

    def testVerifyLockedLogin(self):
        self.loginPage2.Login('locked_out_user', 'secret_sauce')
        self.welcomPage2.verifyTitle()

    def tearDown(self):
        self.base.seleniumEnd(self.driver)


    def testVerifyLockedLogin(self):
        driver = webdriver.Chrome(
            service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        driver.get('https://demo.applitools.com/')
        driver.maximize_window()
        user = driver.find_element(By.ID, "username")
        user.click()
        user.clear()
        user.send_keys("A")
        password = driver.find_element(By.ID, "password")
        password.click()
        password.clear()
        password.send_keys("6")
        signInButton = driver.find_element(By.ID, 'log-in')
        signInButton.click()
        searchButton = driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Start typing to search...']")
        searchButton.click()
        searchButton.clear()
        searchButton.send_keys('Watermelon')
        financialOverview = driver.find_element(By.CSS_SELECTOR, 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > h6.element-header')
        costumerDetails = driver.find_element(By.CSS_SELECTOR, "div[class*='logged-user-n']")
