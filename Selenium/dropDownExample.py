# selenium 4
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.get('https://www.calculator.net/')
driver.maximize_window()
interestCalculatorButtonLink = driver.find_element(By.LINK_TEXT, "Interest Calculator")
interestCalculatorButtonLink.click()

ccompoundSelect = Select(driver.find_element(By.ID, 'ccompound'))
ccompoundSelect.select_by_index(2)
ccompoundSelect.select_by_visible_text("daily")
radioButton = driver.find_elements(By.CLASS_NAME, 'rbmark')
radioButton[1].click()

driver.close()
