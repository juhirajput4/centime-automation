from selenium.webdriver.common.by import By


class AddProductsLocators:
    shop_field = (By.LINK_TEXT, "Shop")
    products_list = (By.XPATH, "//ul[@class='products masonry-done']/li")
    name = (By.XPATH,"//ul[@class='products masonry-done']/li/a/h3")
    addToBasketButton = (By.XPATH,"/a[@rel='nofollow']")
    addToBasketButtonList = (By.XPATH, "//*[@id='content']/ul/li/a[@rel='nofollow']")
    basketButton = (By.XPATH, "//*[@id='wpmenucartli']/a")
    cartItemList = (By.XPATH, "//*[@id='page-34']/div/div[1]/form/table/tbody/tr[@class='cart_item']")
    cartItemRemoveButtons = (By.XPATH, "//td[@class='product-remove']/a")
