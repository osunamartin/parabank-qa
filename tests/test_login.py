from pages.login_page import LoginPage


def test_login_valid_user(driver):
    """
    Verifies that valid credentials redirect the user to the Accounts Overview page.
    Uses the pre-seeded ParaBank demo account (john / demo).
    """
    login_page = LoginPage(driver)
    login_page.login("john", "demo")

    assert "Accounts Overview" in driver.page_source


def test_login_empty(driver):
    """
    Verifies that leaving empty fields shows an error message stating username and password are required.
    """
    login_page = LoginPage(driver)
    login_page.login("", "")

    error_message = login_page.get_error_message()
    assert "enter a username and password" in error_message
