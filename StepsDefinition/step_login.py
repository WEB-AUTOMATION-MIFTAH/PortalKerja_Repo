import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from Pages.basemethod import CustomMethod
from Pages.login import LocatorLoginModal

class StepDefLogin(CustomMethod, LocatorLoginModal):

    def __init__(self, driver):
        super().__init__(driver)

    def check_email_field_is_exist(self):
        self.is_web_element_visible(self.LOC_EMAIL_FIELD)

    def check_pwd_field_is_exist(self):
        self.is_web_element_visible(self.LOC_PWD_FIELD)

    def check_login_btn_is_exist(self):
        self.is_web_element_visible(self.LOC_LOGIN_BTN)

    def check_logo_is_exist(self):
        self.is_web_element_visible(self.LOC_LOGO_POKER)

    def user_do_login(self, email, password):
        self.fill_in(self.LOC_EMAIL_FIELD, email)
        self.fill_in(self.LOC_PWD_FIELD, password)
        self.click_to(self.LOC_LOGIN_BTN)