from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 20


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def click(self, locator):
        """Wait for the element to be clickable, then click it."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        """Wait for the element to be visible, clear it, then type text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Wait for the element to be visible and return its text."""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        """Return True if the element becomes visible within the timeout, False otherwise."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def find_elements(self, locator):
        """Wait for at least one matching element to be present, then return all."""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
        except Exception:
            pass
        return self.driver.find_elements(*locator)
