from selenium.webdriver.common.by import By


class AddAddressLocators:
    addressButton = (By.XPATH, "(//nav[@class='woocommerce-MyAccount-navigation']/ul/li)[4]/a")
    editButton = (By.XPATH, "(//header[@class='woocommerce-Address-title title']/a)[1]")
    billingFirstName= (By.XPATH, "//input[@id='billing_first_name']")
    billingLastName =(By.XPATH, "//input[@id='billing_last_name']")
    billingPhone = (By.XPATH, "//input[@id='billing_phone']")
    billingAddress= (By.XPATH, "//input[@placeholder='Street address']")
    billingCity = (By.XPATH, "//input[@id='billing_city']")
    billingPostcode = (By.XPATH, "//input[@id='billing_postcode']")
    saveAddress= (By.XPATH, "//input[@name='save_address']")

    completeAddress = (By.XPATH, "//div[@class='u-column1 col-1 woocommerce-Address']/address")