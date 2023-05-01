# selenium 4
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.get('https://shop.demoqa.com/my-account/')
driver.maximize_window()

username = driver.find_element(By.ID, 'reg_username')
username.click()
username.clear()
username.send_keys('ABCDEF1234')

email = driver.find_element(By.ID, 'reg_email')
email.click()
email.clear()
email.send_keys('mwdscgwvnqpvxayovy@tcwlm.com')

password = driver.find_element(By.ID, 'reg_password')
password.click()
password.clear()
password.send_keys('ABCDEF1234!@#$')

registerButton = driver.find_element(By.NAME, 'register')
if registerButton.text == 'Register':
    registerButton.click()
else:
    print('Wrong Button!')

driver.close()


