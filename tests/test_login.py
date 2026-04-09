from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_login_valid_user(driver):

    login_page = LoginPage(driver)

    login_page.login("john", "demo")

    assert "Accounts Overview" in driver.page_source

def test_login_invalid(driver):
    login_page = LoginPage(driver)

    login_page.login("john", "wrong_password")    
    error_message = driver.find_element(By.CLASS_NAME, "error").text
    assert "could not be verified" in error_message

