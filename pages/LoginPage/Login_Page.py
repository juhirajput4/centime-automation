from locators.login_locators import LoginPageLocators
from base.selenium_driver import Selenium_Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_Page(Selenium_Driver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickOnLogoutButton(self):
        self.clickElement(LoginPageLocators.logout_Button)

    def enterUserName(self, email):
        self.sendKeys(email, LoginPageLocators.userName_field)

    def enterPassword(self,password):
        self.sendKeys(password,LoginPageLocators.passWord_field)

    def clickOnLoginButton(self):
        self.clickElement(LoginPageLocators.login_button)