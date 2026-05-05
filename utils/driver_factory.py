import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    service = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()

    if os.getenv("CI"):
        # Headless mode required in GitHub Actions and other CI environments
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    return webdriver.Chrome(service=service, options=options)
