import time

from locators.addProducts_locators import AddProductsLocators
from base.selenium_driver import Selenium_Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

class AddProduct_Page(Selenium_Driver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def clickOnShop(self):
        self.clickElement(AddProductsLocators.shop_field)

    def selectProduct(self, product):
        print("Hello selectProduct")
        products = self.getElementList(AddProductsLocators.addToBasketButtonList)
        productsName = self.getElementList(AddProductsLocators.name)
        print(len(products))
        print(len(productsName))
        print("length of products")

        for i in range(0, len(productsName)):
            if product in productsName[i].text:
                print(productsName[i].text)
                time.sleep(5)
                products[i].click()
                time.sleep(5)

    def gotoActiveBasketList(self):
        self.clickElement(AddProductsLocators.basketButton)

    def checkItemInCartItemList(self, product):
        cartItems = self.getElementList(AddProductsLocators.cartItemList)
        time.sleep(5)
        for item in cartItems:
            if product in item.text:
                return True
        return False

    def removeItemFromCart(self,product):
        cartItems = self.getElementList(AddProductsLocators.cartItemList)
        removeButtons = self.getElementList(AddProductsLocators.cartItemRemoveButtons)
        time.sleep(5)
        for i in range(0, len(cartItems)):
            if product in cartItems[i].text:
                removeButtons[i].click()
