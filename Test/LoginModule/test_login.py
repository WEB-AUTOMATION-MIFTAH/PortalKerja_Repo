import pytest
from Test.object_instance import ObjectInstantiation

@pytest.mark.usefixtures("setup_scope_function")
class TestLoginModalFunctionality(ObjectInstantiation):

    @pytest.mark.smoke
    def test_login_superadmin(self):
        self.landingf().click_to_login_button()
        self.loginf().login_as_super_admin_vpn27()


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