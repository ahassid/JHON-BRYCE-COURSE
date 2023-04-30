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
salaryButtonLink = driver.find_element(By.LINK_TEXT, "Salary Calculator")
salaryButton_text = salaryButtonLink.text
if salaryButton_text == 'Salary Calculator':
    print('Text appears as expected')
else:
    print('Text not found')
salaryButtonLink.click()
fitnessButtonLink = driver.find_element(By.PARTIAL_LINK_TEXT, "Fitness")
fitnessButtonLink.click()

driver.close()
