from selenium.webdriver.common.by import By


class AddProductsLocators:
    shop_field = (By.LINK_TEXT, "Shop")
    products_list = (By.XPATH, "//ul[@class='products masonry-done']/li")

