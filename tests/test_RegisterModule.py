
from selenium.webdriver.common.by import By
import time
import pytest
import unittest


@pytest.mark.usefixtures("setupDriver")
class loginTest(unittest.TestCase):
    validEmailId = "juhi.rajput@cloudanalogy.com"
    validPss = "juhirajput57"

    # invalidEmailId = "rajput@cloudanalogy.com"
    # invalidPss = "juhirajput57"

    @pytest.fixture(autouse=True)
    def setUpMethod(self, setupDriver):
        self.lp = Login_Page(self.driver)

    # def test_registerWithValid(self):
    #     self.lp.enterRegisterEmail(self.validEmailId)
    #     time.sleep(5)
    #     self.lp.enterRegisterPassword(self.validPss)
    #     actual_Text = self.lp.verify_assertText()
    #     self.assertEqual(actual_Text, "Strong")
    #     self.lp.clickOnRegisterButton()
    #     time.sleep(5)
    #     self.lp.clickOnLogoutButton()

    def test_registerWithInValid(self):
        self.lp.enterRegisterEmail(self.validEmailId)
        time.sleep(5)
        self.lp.enterRegisterPassword(self.validPss)
        # actual_Text = self.lp.verify_assertText()
        # self.assertEqual(actual_Text, "Strong")
        self.lp.clickOnRegisterButton()

        actual_errorText = self.lp.verifyErrorMessage()
        print(actual_errorText)
        self.assertEqual(actual_errorText, "Error:")

        time.sleep(5)


