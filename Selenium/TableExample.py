from selenium.webdriver.common.by import By
from PageObject.Tests.PageObjectBase import PageObjectBase

base = PageObjectBase()
driver = base.seleniumStart('https://demo.applitools.com/app.html')
table = driver.find_element(By.CSS_SELECTOR, 'table[class="table table-padded"]')
print(table.text)  # prints all the table
rows = table.find_elements(By.TAG_NAME, 'tr')
cells = rows[1].find_elements(By.TAG_NAME, 'td')
cellTest = cells[2]
print(cellTest.text)  # print cell number 3 in row number 2
base.seleniumEnd(driver)
