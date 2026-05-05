from pages.accounts_page import AccountsPage


def test_accounts_overview_displays_after_login(logged_in_driver):
    """
    Verifies that the Accounts Overview page is shown immediately after login,
    confirming that the heading text and the accounts table are both present.
    """
    accounts_page = AccountsPage(logged_in_driver)

    assert "Accounts Overview" in logged_in_driver.page_source
    assert accounts_page.is_account_table_visible()


def test_accounts_table_contains_account_links(logged_in_driver):
    """
    Verifies that john's account table has at least one clickable account link,
    confirming that the demo data was loaded correctly.
    """
    accounts_page = AccountsPage(logged_in_driver)
    links = accounts_page.get_account_links()

    assert len(links) > 0


def test_open_new_checking_account(logged_in_driver):
    """
    Verifies that a logged-in user can open a new CHECKING account.
    After the AJAX call completes, the confirmation panel appears and the
    new account ID is a numeric string.
    """
    accounts_page = AccountsPage(logged_in_driver)
    accounts_page.navigate_to_open_account()
    accounts_page.open_new_account("CHECKING")

    assert accounts_page.is_account_opened_successfully()
    new_id = accounts_page.get_new_account_id()
    assert new_id.isdigit(), f"Expected a numeric account ID, got: {new_id!r}"


def test_open_new_savings_account(logged_in_driver):
    """
    Verifies that a logged-in user can open a new SAVINGS account.
    Mirrors the CHECKING test to ensure both account types go through
    the same successful flow.
    """
    accounts_page = AccountsPage(logged_in_driver)
    accounts_page.navigate_to_open_account()
    accounts_page.open_new_account("SAVINGS")

    assert accounts_page.is_account_opened_successfully()
    new_id = accounts_page.get_new_account_id()
    assert new_id.isdigit(), f"Expected a numeric account ID, got: {new_id!r}"
