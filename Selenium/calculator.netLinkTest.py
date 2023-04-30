# selenium 4
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.get('https://www.calculator.net/')
driver.maximize_window()
salaryButton = driver.find_element(By.LINK_TEXT, "Salary Calculator")
salaryButton_text = salaryButton.text
if salaryButton_text == 'Salary Calculator':
    print('salary calculator text appears as expected')
salaryButton.click()
salaryButton = driver.find_element(By.PARTIAL_LINK_TEXT, "Fitness")
salaryButton.click()

driver.close()
