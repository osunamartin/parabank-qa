from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10


def wait_for_element(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until the element is visible in the DOM."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until the element is visible and enabled."""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_text_in_element(driver, locator, text, timeout=DEFAULT_TIMEOUT):
    """Wait until the given text appears inside the element."""
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element(locator, text)
    )


def wait_for_url_contains(driver, url_fragment, timeout=DEFAULT_TIMEOUT):
    """Wait until the current URL contains the given fragment."""
    return WebDriverWait(driver, timeout).until(
        EC.url_contains(url_fragment)
    )
