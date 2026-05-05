from pages.login_page import LoginPage


def test_login_valid_user(driver):
    """
    Verifies that valid credentials redirect the user to the Accounts Overview page.
    Uses the pre-seeded ParaBank demo account (john / demo).
    """
    login_page = LoginPage(driver)
    login_page.login("john", "demo")

    assert "Accounts Overview" in driver.page_source


def test_login_invalid(driver):
    """
    Verifies that an incorrect password triggers an inline error message
    stating that credentials could not be verified.
    """
    login_page = LoginPage(driver)
    login_page.login("john", "wrong_password")

    error_message = login_page.get_error_message()
    assert "could not be verified" in error_message
