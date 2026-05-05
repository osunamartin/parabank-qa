from pages.register_page import RegisterPage
from test_data.users import generate_new_user, VALID_USER


def test_register_new_user_successfully(driver):
    """
    Happy-path: a brand-new user fills out every field of the registration form
    with valid data and is greeted by a welcome message after submission.
    A random username suffix is generated on each run to avoid duplicate collisions
    against the stateful ParaBank demo server.
    """
    register_page = RegisterPage(driver)
    register_page.navigate()

    new_user = generate_new_user()
    register_page.register(new_user)

    assert "Welcome" in driver.page_source


def test_register_duplicate_username_shows_error(driver):
    """
    Verifies that attempting to register with an already-taken username (john)
    returns a field-level error rather than creating a duplicate account.
    """
    register_page = RegisterPage(driver)
    register_page.navigate()

    duplicate_user = generate_new_user()
    duplicate_user["username"] = VALID_USER["username"]  # "john" already exists
    register_page.register(duplicate_user)

    error_text = register_page.get_username_error()
    assert "already exists" in error_text


def test_register_blank_form_shows_validation_errors(driver):
    """
    Verifies that submitting the registration form without filling any field
    triggers client-side / server-side validation and displays required-field
    errors. We check the First Name error as a representative example.
    """
    register_page = RegisterPage(driver)
    register_page.navigate()
    register_page.submit()  # click Register with all fields empty

    error_text = register_page.get_first_name_error()
    assert "required" in error_text.lower()
