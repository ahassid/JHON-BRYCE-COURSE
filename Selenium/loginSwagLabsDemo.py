# selenium 4
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
user = driver.find_element(By.ID, "user-name")
user.click()
user.clear()
# search.send_keys("standard_user")
user.send_keys("problem_user")
password = driver.find_element(By.ID, "password")
password.click()
password.clear()
password.send_keys("secret_sauce")
login = driver.find_element(By.ID, "login-button")
login_text = login.accessible_name
if login_text == 'Login':
    print('login text appears as expected')
login.click()

menu = driver.find_element(By.ID, "react-burger-menu-btn")
menu.click()
img = driver.find_element(By.ID, "item_1_img_link")
img.click()

driver.close()
