from selenium.webdriver.common.by import By


class TransferLocators:
    AMOUNT           = (By.ID, "amount")
    FROM_ACCOUNT     = (By.ID, "fromAccountId")
    TO_ACCOUNT       = (By.ID, "toAccountId")
    TRANSFER_BUTTON  = (By.XPATH, "//input[@value='Transfer']")
    SUCCESS_HEADING  = (By.XPATH, "//h1[contains(text(),'Transfer Complete')]")
