from locators.login_locators import LoginPageLocators
from base.selenium_driver import Selenium_Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_Page(Selenium_Driver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def enterRegisterEmail(self, registerEmail):
        self.sendKeys(registerEmail, LoginPageLocators.register_emailId)

    def enterRegisterPassword(self,registerPassword):
        self.sendKeys(registerPassword,LoginPageLocators.register_password)

    def verify_assertText(self):
        self.getText(LoginPageLocators.strong_text)

    def clickOnRegisterButton(self):
        self.clickElement(LoginPageLocators.register_button)

    # def verifyErrorMessage(self):
    #     # self.getText(LoginPageLocators.error_message)
    #     return self.driver.findElement(By.XPATH, "(//ul[@class='woocommerce-error']/li/strong)[1]").getText()
    def clickOnLogoutButton(self):
        self.clickElement(LoginPageLocators.logout_Button)

    def enterUserName(self, email):
        self.sendKeys(email, LoginPageLocators.userName_field)

    def enterPassword(self,password):
        self.sendKeys(password,LoginPageLocators.passWord_field)

    def clickOnLoginButton(self):
        self.clickElement(LoginPageLocators.login_button)