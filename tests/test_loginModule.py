from pages.LoginPage.Login_Page import Login_Page
from configurations.LoginPage import emailId, validPassword, userName,invalidPassword
from pages.AddProductPage.Add_Product_Page import AddProduct_Page

import time
import pytest
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setupDriver")
class loginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setUpMethod(self, setupDriver):
        self.lp = Login_Page(self.driver)
        self.driver = self.driver

    #@pytest.mark.run(order=1)
    def test_valid_Login(self):
      self.lp.enterUserName(emailId)
      self.lp.enterPassword(validPassword)
      self.lp.clickOnLoginButton()
      WebDriverWait(self.driver, 20).until(
          EC.presence_of_element_located((By.XPATH, "//div[@class='woocommerce-MyAccount-content']/p"))
      )

      element = self.driver.find_element(By.XPATH, "//div[@class='woocommerce-MyAccount-content']/p")

      assert userName in element.text

    #@pytest.mark.run(order=2)
    def test_invalid_Login(self):
      self.lp.enterUserName(emailId)
      self.lp.enterPassword(invalidPassword)
      self.lp.clickOnLoginButton()
      WebDriverWait(self.driver, 20).until(
          EC.presence_of_element_located((By.XPATH, "//div[@class='woocommerce']/ul/li"))
      )

      element = self.driver.find_element(By.XPATH, "//div[@class='woocommerce']/ul/li")

      assert 'Error' in element.text


    # def test_registerWithValid(self):
    #     self.lp.enterRegisterEmail(self.validEmailId)
    #     time.sleep(5)
    #     self.lp.enterRegisterPassword(self.validPss)
    #     actual_Text = self.lp.verify_assertText()
    #     self.assertEqual(actual_Text, "Strong")
    #     self.lp.clickOnRegisterButton()
    #     time.sleep(5)
    #     self.lp.clickOnLogoutButton()


    # def test_invalid_Login(self):
    #     self.lp.enterUserName(self.emailId)
    #     self.lp.enterPassword("djees")


    # def test_valid_Login(self):
    #     self.lp.enterUserName(self.emailId)
    #     self.lp.enterPassword(self.pss)
    #     print(self.emailId)
    #
    #     addProdToCart = AddProduct_Page(self.driver)
    #     addProdToCart.clickOnShop()
    #     time.sleep(3)
    #     addProdToCart.selectProduct(self.product)

    # def add_To_Cart(self):
    #     addProdToCart = AddProduct_Page(self.driver)
    #     addProdToCart.selectProduct(self.product)






