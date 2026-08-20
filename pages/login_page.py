from selenium.webdriver.common.by import By



class LoginPage:
    NAV_LOGIN_BTN = (By.XPATH, "//a[@href='/login']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    YALLA_BTN = (By.XPATH, "//button[@type='submit']")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR,"h3")
    OK_BTN = (By.XPATH,"//*button[@text ='OK']")

    def __init__(self, driver):
        self.driver = driver

    def open_login_form(self):
        self.driver.find_element(*self.NAV_LOGIN_BTN).click()

    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.YALLA_BTN).click()

    def login(self,email,password):
        self.fill_email(email)
        self.fill_password(password)
        self.submit_login()

    def loggin_success_text(self):
        return self.driver.find_element(*self.CONFIRMATION_TEXT).text

    def close_window(self):
        self.driver.find_element(*self.OK_BTN).click()