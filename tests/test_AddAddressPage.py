from selenium.webdriver.common.by import By
import time
import pytest
import unittest

from configurations.LoginPage import emailId, validPassword

from pages.AddAddressPage.Add_Address_Page import AddAddressPage
from pages.LoginPage.Login_Page import Login_Page


@pytest.mark.usefixtures("setupDriver")
class AddAddressPageTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setUpMethod(self, setupDriver):
        self.addAddressPage = AddAddressPage(self.driver)

    def test_add_products_with_valid(self):
        loginPage = Login_Page(self.addAddressPage.driver)
        loginPage.enterUserName(emailId)
        # time.sleep(5)
        loginPage.enterPassword(validPassword)
        # time.sleep(5)
        loginPage.clickOnLoginButton()
        # time.sleep(5)
        print('test_add_address_with_valid')
        self.addAddressPage.clickOnAddressButton()
        time.sleep(5)
        # self.addAddressPage.clickOnEditButton()
        # time.sleep(5)
        # self.addAddressPage.fillBillingAddressForm()
        # time.sleep(5)
        # self.addAddressPage.clickOnAddressButton()
        # time.sleep(5)
        isValid = self.addAddressPage.verifyAddress()
        time.sleep(5)
        assert isValid == True





