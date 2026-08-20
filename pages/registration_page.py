from selenium.webdriver.common.by import By

class SignupPage:
    NAV_SIGNUP_BTN = (By.XPATH, "//a[@href='/register']")
    NAME_INPUT = (By.XPATH, "//input[@name='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@name='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    TERMS_OF_USE_INPUT = (By.XPATH, "//input[@id='terms-of-use']")
    YALLA_BTN = (By.XPATH, "//button[@type='submit']")
    FAILED_TEXT = (By.XPATH, "//div[@role='dialog']")
    OK_BTN = (By.XPATH, "//button[text() = 'OK']")

    def __init__(self, driver):
        self.driver = driver

    def open_signup_form(self):
        self.driver.find_element(*self.NAV_SIGNUP_BTN).click()

    def fill_name(self, name):
        self.driver.find_element(*self.NAME_INPUT).clear()
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    def fill_lastname(self, lastname):
        self.driver.find_element(*self.LASTNAME_INPUT).clear()
        self.driver.find_element(*self.LASTNAME_INPUT).send_keys(lastname)

    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)


    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def select_terms_of_use(self):
        self.driver.find_element(*self.TERMS_OF_USE_INPUT).click()

    def submit_register(self):
        self.driver.find_element(*self.YALLA_BTN).click()

   # def loggin_success_text(self):
   #     return self.driver.find_element(*self.CONFIRMATION_TEXT).text

    def register(self, name, lastname, email, password):
        self.fill_name(name)
        self.fill_lastname(lastname)
        self.fill_email(email)
        self.fill_password(password)
        self.select_terms_of_use()
        self.submit_register()

    def loggin_failed_text(self):
        return self.driver.find_element(*self.FAILED_TEXT).text

    def close_window(self):
        self.driver.find_element(*self.OK_BTN).click()