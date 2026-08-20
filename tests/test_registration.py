from pages.registration_page import SignupPage
VALID_NAME = 'Valentine'
VALID_LAST_NAME = 'Huts'
VALID_EMAIL =  'valikguts@gmail.com'
VALID_PASSWORD = 'ValentineHuts*3'

INVALID_NAME = '1'
INVALID_LAST_NAME = '12345'
INVALID_EMAIL =  'valikguts@gmail.com' #already registred mail
INVALID_PASSWORD = 'Valik 1!'


def test_registration_invalid_name(driver):
    signup_page = SignupPage(driver)

    signup_page.open_signup_form()
    signup_page.register(INVALID_NAME,VALID_LAST_NAME,VALID_EMAIL,VALID_PASSWORD)

    assert "Registration failed" in signup_page.loggin_failed_text()

    signup_page.close_window()


def test_registration_invalid_last_name(driver):
    signup_page = SignupPage(driver)

    signup_page.open_signup_form()
    signup_page.register(VALID_NAME,INVALID_LAST_NAME,VALID_EMAIL,VALID_PASSWORD)

    assert "Registration failed" in signup_page.loggin_failed_text()

    signup_page.close_window()

def test_registration_invalid_email(driver):
    signup_page = SignupPage(driver)

    signup_page.open_signup_form()
    signup_page.register(VALID_NAME,VALID_LAST_NAME,INVALID_EMAIL,VALID_PASSWORD)

    assert "Registration failed" in signup_page.loggin_failed_text()

    signup_page.close_window()

def test_registration_invalid_password(driver):
    signup_page = SignupPage(driver)

    signup_page.open_signup_form()
    signup_page.register(VALID_NAME,VALID_LAST_NAME,VALID_EMAIL,INVALID_PASSWORD)

    assert "Registration failed" in signup_page.loggin_failed_text()

    signup_page.close_window()