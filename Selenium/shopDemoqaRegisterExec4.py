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

detailsDriver = webdriver.Chrome(
    service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
detailsDriver.get('https://www.minuteinbox.com/')
detailsDriver.maximize_window()

allDetails = detailsDriver.find_element(By.ID, 'email')
allDetailsText = allDetails.text
allDetailsLength = len(allDetailsText)
user = allDetailsText[0:round(allDetailsLength / 2)]
userPassword = allDetailsText[round(allDetailsLength / 2): (allDetailsLength - 1)]

username = driver.find_element(By.ID, 'reg_username')
username.click()
username.clear()
# username.send_keys('ABCDE12345')
username.send_keys(user)

email = driver.find_element(By.ID, 'reg_email')
email.click()
email.clear()
# email.send_keys('mwdscgwvnqpvxayovy2@tcwlm.com')
email.send_keys(allDetailsText)

password = driver.find_element(By.ID, 'reg_password')
password.click()
password.clear()
# password.send_keys('ABCDE12345!@#$%')
password.send_keys(userPassword)


registerButton = driver.find_element(By.NAME, 'register')
if registerButton.text == 'Register':
    registerButton.click()
    # registerButton.submit()
else:
    print('Wrong Button!')

driver.close()
