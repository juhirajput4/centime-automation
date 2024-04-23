import os
import logging

from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class Selenium_Driver():

    def __init__(self, driver):
        self.driver = driver

    def getElement(self, locator):
        element = None
        element = self.driver.find_element(*locator)
        print("Element Found with locator: " + locator[1])
        return element

    def clickElement(self, locator):
        self.getElement(locator).click()
    def sendKeys(self, data, locator):
        element = self.getElement(locator)
        element.send_keys(data)
        print("Sent data on element with locator: " + locator[1])

    def getText(self, locator):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            element = self.getElement(locator)
            self.highlight_element(locator)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            else:
                print("Getting text on element :: " + locator[1])
                print("The text is :: '" + text + "'")
                text = text.strip()
        except Exception as err_msg:
            raise AssertionError("Failed to get text on element: " + locator[1] + "\nerror:" + str(err_msg))
        return text

    def getElementList(self, locator):
        """
        Get list of elements
        """
        elements = self.driver.find_elements(*locator)
        if (elements):
            print("Element list FOUND with locator: " + locator[1])
        else:
            print("Element list NOT FOUND with locator: " + locator[1])
        return elements

    def isElementPresent(self, locator):
        try:
            elements = self.driver.find_elements(*locator)
            if (elements):
                self.log.info("Element Found: " + str(locator))
                return True
            else:
                self.log.info("Element not found: " + str(locator))
                return False
        except:
            self.log.info("Element not found: " + str(locator))
            return False
