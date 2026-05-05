from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from locators.transfer_locators import TransferLocators
from utils.config import TRANSFER_URL


class TransferPage(BasePage):

    def navigate(self):
        self.driver.get(TRANSFER_URL)

    def transfer_funds(self, amount, from_index=0, to_index=1):
        """
        Enter the transfer amount and select source/destination accounts by
        their dropdown index, then submit the form.
        """
        self.type(TransferLocators.AMOUNT, str(amount))
        self.wait.until(
            lambda d: len(Select(d.find_element(*TransferLocators.FROM_ACCOUNT)).options) > 0
        )
        Select(self.driver.find_element(*TransferLocators.FROM_ACCOUNT)).select_by_index(from_index)
        Select(self.driver.find_element(*TransferLocators.TO_ACCOUNT)).select_by_index(to_index)
        self.click(TransferLocators.TRANSFER_BUTTON)

    def is_transfer_complete(self):
        """Return True if the 'Transfer Complete!' heading becomes visible."""
        return self.is_visible(TransferLocators.SUCCESS_HEADING)

    def get_success_heading(self):
        return self.get_text(TransferLocators.SUCCESS_HEADING)
