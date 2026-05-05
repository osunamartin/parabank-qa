import os

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from test_data.users import VALID_USER
from utils.config import BASE_URL
from utils.driver_factory import create_driver

os.makedirs("reports", exist_ok=True)


@pytest.fixture
def driver():
    """
    Session-scoped Chrome driver that opens the ParaBank home page.
    Automatically quits the browser after each test.
    """
    driver = create_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    """
    Reuses the driver fixture and authenticates as the demo user 'john'
    before yielding. Use this for any test that requires an active session.
    """
    login_page = LoginPage(driver)
    login_page.login(VALID_USER["username"], VALID_USER["password"])
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "accountTable"))
    )
    yield driver
