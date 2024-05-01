import time

from locators.addressPage_locators import AddAddressLocators
from base.selenium_driver import Selenium_Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

class AddAddressPage(Selenium_Driver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def clickOnAddressButton(self):
        self.clickElement(AddAddressLocators.addressButton)

    def clickOnEditButton(self):
        self.clickElement(AddAddressLocators.editButton)

    def fillBillingAddressForm(self):
        self.sendKeys('Juhi',AddAddressLocators.billingFirstName)
        time.sleep(5)
        self.sendKeys('Rajput', AddAddressLocators.billingLastName)
        time.sleep(5)
        self.sendKeys('707070', AddAddressLocators.billingPhone)
        time.sleep(5)
        self.sendKeys('Noida', AddAddressLocators.billingAddress)
        time.sleep(5)
        self.sendKeys('Noida', AddAddressLocators.billingCity)
        time.sleep(5)
        self.sendKeys('201001', AddAddressLocators.billingPostcode)
        time.sleep(5)
        self.clickElement(AddAddressLocators.saveAddress)

    def verifyAddress(self):
        address = self.getElementList(AddAddressLocators.completeAddress)
        time.sleep(5)

        for i in range(0, len(address)):
            print(address[i].text)
            if 'Juhi Rajput' in address[i].text:
                return True

        return False

