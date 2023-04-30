# selenium 4
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.get('http://google.com')
search = driver.find_element(By.NAME, "q")
search.click()
search.clear()
search.send_keys("gal")
search.send_keys(Keys.ENTER)
driver.close()
