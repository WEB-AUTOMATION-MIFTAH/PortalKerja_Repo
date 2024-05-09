from Pages.basemethod import CustomMethod
from Pages.loginmodalpage import LocLoginPage

class StepDefLogin(CustomMethod, LocLoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_email_field_is_exist(self):
        self.is_web_element_visible(self.LOC_EMAIL_FIELD)

    def check_pwd_field_is_exist(self):
        self.is_web_element_visible(self.LOC_PWD_FIELD)

    def check_login_btn_is_exist(self):
        self.is_web_element_visible(self.LOC_LOGIN_BTN)

    def check_copywriting_login_button(self):
        pass

    def check_copywriting_title_modal_login(self):
        pass

    def check_copywriting_subtitle_modal_login(self):
        pass

    def check_copywriting_email_field_label(self):
        pass

    def check_copywriting_password_field_label(self):
        pass

    def check_copywriting_email_field_placeholder(self):
        pass

    def check_copywriting_password_field_placeholder(self):
        pass

    def check_copywriting_forgot_password_linktext(self):
        pass

    def check_copywriting_new_user_text(self):
        pass

    def check_copywriting_signup_free_now(self):
        pass