from selenium.webdriver.common.by import By
import time
import pytest
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configurations.RegisterPage import validEmailIdToRegister, validPasswordToRegister, validRegisteredUserName, invalidEmailIdToRegister, invalidPasswordToRegister
from pages.RegisterPage.Register_Page import Register_Page


@pytest.mark.usefixtures("setupDriver")
class registerTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setUpMethod(self, setupDriver):
        self.registerPage = Register_Page(self.driver)

    def test_register_with_valid(self):
        self.registerPage.enterEmailToRegister(validEmailIdToRegister)
        time.sleep(5)
        self.registerPage.enterPasswordToRegister(validPasswordToRegister)
        self.registerPage.clickOnRegisterButton()
        WebDriverWait(self.registerPage.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='woocommerce-MyAccount-content']/p"))
        )

        element = self.registerPage.driver.find_element(By.XPATH, "//div[@class='woocommerce-MyAccount-content']/p")

        assert validRegisteredUserName in element.text




