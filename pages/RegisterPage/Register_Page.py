from locators.registerPage_locators import RegisterPageLocators
from base.selenium_driver import Selenium_Driver

class Register_Page(Selenium_Driver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def enterEmailToRegister(self, registerEmail):
        self.sendKeys(registerEmail, RegisterPageLocators.register_emailId)

    def enterPasswordToRegister(self, registerPassword):
        self.sendKeys(registerPassword,RegisterPageLocators.register_password)

    def clickOnRegisterButton(self):
        self.clickElement(RegisterPageLocators.register_button)

