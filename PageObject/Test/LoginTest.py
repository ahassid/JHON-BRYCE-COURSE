from PageObject.Pages.LoginPage import LoginPage
from PageObject.Tests.PageObjectBase import PageObjectBase

base = PageObjectBase()
driver = base.seleniumStart('https://www.saucedemo.com/')
loginPage = LoginPage(driver)
loginPage.Login('performance_glitch_user', 'secret_sauce')

base.seleniumEnd(driver)
