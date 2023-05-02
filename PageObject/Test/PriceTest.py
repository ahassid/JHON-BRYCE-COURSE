from PageObject.Pages.LoginPage import LoginPage
from PageObject.Pages.WelcomePage import WelcomePage
from PageObject.Tests.PageObjectBase import PageObjectBase

base = PageObjectBase()

driver = base.seleniumStart('https://www.saucedemo.com/')
LoginPage = LoginPage(driver)
LoginPage.Login('performance_glitch_user', 'secret_sauce')

WelcomePage = WelcomePage(driver)
productsPrices = WelcomePage.Welcome()

for price in productsPrices:
    assert price.text == '$29.99', 'The price of this product is differ than $29.99'
    print(price.text)

# assert productsPrices[1].text == '$9.99', 'The price of product number 2 wrong'
# assert productsPrices[3].text == '$9.99', 'The price of product number 4 wrong'

base.seleniumEnd(driver)
