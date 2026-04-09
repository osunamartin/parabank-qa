import pytest
from utils.driver_factory import create_driver


@pytest.fixture
def driver():
    driver = create_driver()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    yield driver

    driver.quit()
