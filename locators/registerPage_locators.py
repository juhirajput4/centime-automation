from selenium.webdriver.common.by import By


class RegisterPageLocators:
    register_emailId = (By.ID, "reg_email")
    register_password = (By.ID, "reg_password")
    strong_text = (By.CLASS_NAME, "woocommerce-password-strength strong")
    register_button = (By.NAME, "register")
