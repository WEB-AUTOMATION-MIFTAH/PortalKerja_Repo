import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from Pages.basemethod import CustomMethod
from Pages.login import LocatorLoginPage


class StepDefLogin(CustomMethod, LocatorLoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_email_field(self):
        pass

    def check_pwd_field(self):
        pass

    def check_login_btn(self):
        pass

    def check_logo(self):
        pass

    def user_do_login(self, fill_in_email, fill_in_Passwd):
        self.fill_in(self.LOC_EMAIL_FIELD, fill_in_email)
        self.fill_in(self.LOC_PWD_FIELD, fill_in_Passwd)
        self.click_to(self.LOC_LOGIN_BTN)