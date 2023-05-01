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

search = driver.find_element(By.ID, 'calcSearchTerm')
search.click()
search.clear()
search.send_keys('michael')

result = driver.find_element(By.ID, 'calcSearchOut')
resultText = result.text
print(resultText)

driver.close()


