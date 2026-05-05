from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.accounts_locators import AccountsLocators
from utils.config import OPEN_ACCOUNT_URL


class AccountsPage(BasePage):

    # ── Accounts Overview ────────────────────────────────────────────────────

    def get_heading(self):
        return self.get_text(AccountsLocators.PAGE_HEADING)

    def is_account_table_visible(self):
        return self.is_visible(AccountsLocators.ACCOUNT_TABLE)

    def get_account_links(self):
        """Return all <a> elements inside the accounts table body."""
        return self.find_elements(AccountsLocators.ACCOUNT_LINKS)

    # ── Open New Account ─────────────────────────────────────────────────────

    def navigate_to_open_account(self):
        self.driver.get(OPEN_ACCOUNT_URL)

    def open_new_account(self, account_type="CHECKING"):
        """Select account type (CHECKING or SAVINGS) and submit the form."""
        type_value = "0" if account_type == "CHECKING" else "1"
        self.wait.until(EC.visibility_of_element_located(AccountsLocators.ACCOUNT_TYPE))
        self.wait.until(
            lambda d: len(Select(d.find_element(*AccountsLocators.FROM_ACCOUNT)).options) > 0
        )
        Select(self.driver.find_element(*AccountsLocators.ACCOUNT_TYPE)).select_by_value(type_value)
        self.click(AccountsLocators.OPEN_BUTTON)

    def is_account_opened_successfully(self):
        """Return True if the account-opened result panel becomes visible."""
        return self.is_visible(AccountsLocators.OPEN_RESULT)

    def get_new_account_id(self):
        """Return the new account number shown in the confirmation panel."""
        return self.get_text(AccountsLocators.NEW_ACCOUNT_ID)
