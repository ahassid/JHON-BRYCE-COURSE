# selenium 4
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.get('https://demo.guru99.com/test/newtours/reservation.php')
driver.maximize_window()

radioFlightType = driver.find_element(By.NAME, 'tripType')
if radioFlightType.is_selected():
    print('This is a Round Trip Ticket')
else:
    print('This is a One Way Ticket')

passengersSelect = Select(driver.find_element(By.NAME, 'passCount'))
passengersSelect.select_by_index(3)

departSelect = Select(driver.find_element(By.NAME, 'fromPort'))
departSelect.select_by_visible_text('Sydney')

returningMonth = Select(driver.find_element(By.NAME, 'toMonth'))
returningMonth.select_by_visible_text('November')

returningDay = Select(driver.find_element(By.NAME, 'toDay'))
returningDay.select_by_index(26)

radioServiceClass = driver.find_elements(By.CLASS_NAME, 'servClass')
radioServiceClass[2].click()

driver.close()
