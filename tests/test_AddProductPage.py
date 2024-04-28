from selenium.webdriver.common.by import By
import time
import pytest
import unittest

from configurations.LoginPage import emailId, validPassword


from pages.AddProductPage.Add_Product_Page import AddProduct_Page
from pages.LoginPage.Login_Page import Login_Page


@pytest.mark.usefixtures("setupDriver")
class AddProductPageTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setUpMethod(self, setupDriver):
        self.addProductPage = AddProduct_Page(self.driver)

    def test_add_products_with_valid(self):
        loginPage = Login_Page(self.addProductPage.driver)
        loginPage.enterUserName(emailId)
        # time.sleep(5)
        loginPage.enterPassword(validPassword)
        # time.sleep(5)
        loginPage.clickOnLoginButton()
        # time.sleep(5)
        print('test_add_products_with_valid')
        self.addProductPage.clickOnShop()
        time.sleep(5)
        self.addProductPage.selectProduct('Thinking in HTML')
        time.sleep(5)
        self.addProductPage.gotoActiveBasketList()
        time.sleep(5)
        isItemPresent = self.addProductPage.checkItemInCartItemList('Thinking in HTML')
        assert isItemPresent == True

        self.addProductPage.removeItemFromCart('Thinking in HTML')
        time.sleep(5)






