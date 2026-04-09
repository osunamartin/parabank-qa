from pages.login_page import LoginPage

def test_login_valid_user(driver):

    login_page = LoginPage(driver)

    login_page.login("john", "demo")

    assert "Accounts Overview" in driver.page_source
