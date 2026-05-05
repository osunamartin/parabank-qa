from pages.base_page import BasePage
from locators.register_locators import RegisterLocators
from utils.config import REGISTER_URL


class RegisterPage(BasePage):

    def navigate(self):
        self.driver.get(REGISTER_URL)

    def fill_form(self, user_data):
        """Populate every field of the registration form from a user_data dict."""
        self.type(RegisterLocators.FIRST_NAME,       user_data["first_name"])
        self.type(RegisterLocators.LAST_NAME,        user_data["last_name"])
        self.type(RegisterLocators.ADDRESS,          user_data["address"])
        self.type(RegisterLocators.CITY,             user_data["city"])
        self.type(RegisterLocators.STATE,            user_data["state"])
        self.type(RegisterLocators.ZIP_CODE,         user_data["zip_code"])
        self.type(RegisterLocators.PHONE,            user_data["phone"])
        self.type(RegisterLocators.SSN,              user_data["ssn"])
        self.type(RegisterLocators.USERNAME,         user_data["username"])
        self.type(RegisterLocators.PASSWORD,         user_data["password"])
        self.type(RegisterLocators.CONFIRM_PASSWORD, user_data["password"])

    def submit(self):
        self.click(RegisterLocators.REGISTER_BUTTON)

    def register(self, user_data):
        """Fill and submit the registration form in one call."""
        self.fill_form(user_data)
        self.submit()

    def get_success_heading(self):
        return self.get_text(RegisterLocators.SUCCESS_HEADING)

    def get_first_name_error(self):
        """Return the validation error text shown next to the First Name field."""
        return self.get_text(RegisterLocators.FIRST_NAME_ERROR)

    def get_username_error(self):
        """Return the validation error text shown next to the Username field."""
        return self.get_text(RegisterLocators.USERNAME_ERROR)
