import pytest
from selenium import webdriver


@pytest.fixture()
def setupDriver(request):
    print("setup Driver")

    baseURL = "https://practice.automationtesting.in/my-account/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseURL)

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print("tear down")
    driver.quit()
