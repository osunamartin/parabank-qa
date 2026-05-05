from selenium.webdriver.common.by import By


class AccountsLocators:
    # Accounts Overview page
    PAGE_HEADING   = (By.CSS_SELECTOR, "h1.title")
    ACCOUNT_TABLE  = (By.ID, "accountTable")
    ACCOUNT_LINKS  = (By.CSS_SELECTOR, "#accountTable tbody tr td a")

    # Open New Account page
    ACCOUNT_TYPE   = (By.ID, "type")
    FROM_ACCOUNT   = (By.ID, "fromAccountId")
    OPEN_BUTTON    = (By.CSS_SELECTOR, "input[value='Open New Account']")
    OPEN_RESULT    = (By.ID, "openAccountResult")
    NEW_ACCOUNT_ID = (By.ID, "newAccountId")
