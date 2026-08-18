from pages.login_page import LoginPage

VALID_EMAIL =  'valikguts@gmail.com'
VALID_PASSWORD = 'ZeY5DFb4!XU7YG5'

def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.login(VALID_EMAIL,VALID_PASSWORD)
    login_page.submit_login()

def test_login_success_1(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.login(VALID_EMAIL,VALID_PASSWORD)
