from Pages.basemethod import CustomMethod
from Pages.loginmodalpage import LocLoginPage
from Config.dataconfig import TestData

class StepLoginFunc(CustomMethod, LocLoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_error_message_when_login_is_failed_indonesians(self):
        a = self.get_text_of_element(self.LOC_ERROR_MSG_LOGIN)
        assert a == 'Gagal untuk masuk, silakan periksa username dan/atau password kamu!', 'error msg is unexpected!'

    def check_error_message_when_login_is_failed_english(self):
        a = self.get_text_of_element(self.LOC_ERROR_MSG_LOGIN)
        assert a == 'Login failed, please check your username and/or password!', 'error msg is unexpected!'

    def login_with_user_credential(self, email, password):
        self.fill_in(self.LOC_EMAIL_FIELD, email)
        self.fill_in(self.LOC_PWD_FIELD, password)
        self.click_to(self.LOC_LOGIN_BTN)

    def login_as_super_admin_vpn27(self):
        self.login_with_user_credential(TestData.SUPERADMIN_27, TestData.PWD_SUPERADMIN)
        # self.get_text_of_element()
        # --> verifikasi jika login as super admin berhasil dengan assert halaman dashboard hrms

    def login_as_jobseeker_only(self):
        pass

    def login_as_admin_default(self):
        pass

    def login_as_admin_custom_all_module_viewonly(self):
        pass

    def login_as_admin_custom_all_module_fullaccess(self):
        pass

    def login_as_employee_default(self):
        pass

    def login_as_admin_default_child_company(self):
        pass

    def login_as_admin_custom_child_company(self):
        pass
