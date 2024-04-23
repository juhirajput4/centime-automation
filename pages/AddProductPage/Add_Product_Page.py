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
        name = By.XPATH(".//a/h3")
        addToBasketButton = By.XPATH(".//a[@rel='nofollow']")
        products = self.getElementList(AddProductsLocators.products_list)
        print(len(products))
        for prod in products:
            if prod.is_displayed():
                productName = prod.find_element(name).text

                print("Name of the product is " + productName)
                if productName == product:
                    print("--------------->ADIDAS-- " + prod.text)
                    prod.find_element(addToBasketButton).click()
        viewBasketElement = self.driver.find_element(By.XPATH,"//a[@title='View Basket']")
        assert viewBasketElement.is_displayed()
