import pytest
from Config.dataconfig import TestData
from Test.object_instance import ObjectInstantiation

@pytest.mark.usefixtures("setup_scope_function")
class TestLoginModalFunctionality(ObjectInstantiation):

    """ Failed login section """
    @pytest.mark.smoke
    def test_login_with_invalid_password(self):
        self.landingf().click_to_login_button()
        self.loginf().login_with_user_credential(TestData.SUPERADMIN_27, TestData.INVALID_PASSWORD)
        self.loginf().check_error_message_when_login_is_failed_indonesians()

    def test_user_login_using_unverified_candidates_email_account_32b(self):
        self.landingf().click_to_login_button()
        self.loginf().login_with_user_credential(TestData.SUPERADMIN_27, TestData.PASS)
        self.loginf().check_error_message_when_login_is_failed_indonesians()


    '''success login section'''
    @pytest.mark.smoke
    def test_login_superadmin(self):
        self.landingf().click_to_login_button()
        self.loginf().login_as_super_admin_vpn27()
        self.navbarhrmsf().check_role_name_in_navbar_is_superadmin()

@pytest.mark.usefixtures("setup_scope_class")
class TestLoginModalUi(ObjectInstantiation):
    pass
    # def test_precondition_to_access_login_modal(self):
    #     self.landingui.click_to_login_btn()
    #
    # def test_tc_01_there_is_emailfield(self):
    #     self.login().check_email_field_is_exist()
    #
    # def test_tc_02_there_is_passwordfield(self):
    #     self.login().check_pwd_field_is_exist()
    #
    # def test_tc_03_there_is_login_button(self):
    #     self.login().check_login_btn_is_exist()