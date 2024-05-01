from selenium.webdriver.common.by import By


class LoginPageLocators:
    logout_Button = (By.LINK_TEXT, "Logout")
    error_message = (By.XPATH,"(//ul[@class='woocommerce-error']/li/strong)[1]")

    userName_field = (By.ID, "username")
    passWord_field = (By.ID, "password")
    login_button = (By.NAME, "login")
