from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def login(self, username, password):
        self.type(LoginLocators.USERNAME, username)
        self.type(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def get_error_message(self):
        """Return the text of the inline error shown after a failed login attempt."""
        return self.get_text(LoginLocators.ERROR_MESSAGE)
