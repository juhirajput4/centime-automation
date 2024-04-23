from selenium.webdriver.common.by import By


class LoginPageLocators:
    register_emailId = (By.ID, "reg_email")
    register_password = (By.ID, "reg_password")
    strong_text = (By.CLASS_NAME, "woocommerce-password-strength strong")
    register_button = (By.NAME, "register")
    logout_Button = (By.LINK_TEXT, "Logout")
    error_message = (By.XPATH,"(//ul[@class='woocommerce-error']/li/strong)[1]")

    userName_field = (By.ID, "username")
    passWord_field = (By.ID, "password")
    login_button = (By.NAME, "login")
