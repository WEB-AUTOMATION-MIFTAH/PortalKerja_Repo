import pytest
from Test.object_instance import ObjectInstantiation

@pytest.mark.smoke
@pytest.mark.usefixtures("setup_scope_class")
class TestLoginModalUi(ObjectInstantiation):

    def test_precondition_to_access_login_modal(self):
        self.navbar().click_to_login_btn()

    def test_tc_01_there_is_emailfield(self):
        self.login().check_email_field_is_exist()

    def test_tc_02_there_is_passwordfield(self):
        self.login().check_pwd_field_is_exist()

    def test_tc_03_there_is_login_button(self):
        self.login().check_login_btn_is_exist()

# @pytest.mark.smoke
@pytest.mark.usefixtures("setup_scope_function")
class TestLoginModalFunctionality(ObjectInstantiation):

    def test_login_superadmin(self):
        self.navbar().click_to_login_btn()
        self.login().user_do_login('visiprimaqa+27@gmail.com', 'Password123**')
        self.navbar().check_logo_is_exist()