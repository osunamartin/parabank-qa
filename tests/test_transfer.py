from pages.accounts_page import AccountsPage
from pages.transfer_page import TransferPage


def _ensure_two_accounts(driver):
    """
    Helper: open a new CHECKING account so there are at least two accounts
    available in the transfer dropdowns. Necessary because john's second
    account may have been removed between demo resets.
    """
    accounts_page = AccountsPage(driver)
    accounts_page.navigate_to_open_account()
    accounts_page.open_new_account("CHECKING")


def test_transfer_funds_between_accounts(logged_in_driver):
    """
    Happy-path transfer: moves $100 from account index 0 to account index 1.
    The 'Transfer Complete!' heading must appear in the result panel after the
    AJAX call finishes, confirming the transaction was accepted by the server.
    """
    _ensure_two_accounts(logged_in_driver)

    transfer_page = TransferPage(logged_in_driver)
    transfer_page.navigate()
    transfer_page.transfer_funds(amount=100, from_index=0, to_index=1)

    assert transfer_page.is_transfer_complete()


def test_transfer_confirmation_shows_amount(logged_in_driver):
    """
    Verifies that the confirmation message displayed after a successful transfer
    contains the exact amount that was entered ($50.00), proving the server
    echoes back the correct transaction details.
    """
    _ensure_two_accounts(logged_in_driver)

    transfer_page = TransferPage(logged_in_driver)
    transfer_page.navigate()
    transfer_page.transfer_funds(amount=50, from_index=0, to_index=1)

    assert transfer_page.is_transfer_complete()
    assert "50.00" in logged_in_driver.page_source
