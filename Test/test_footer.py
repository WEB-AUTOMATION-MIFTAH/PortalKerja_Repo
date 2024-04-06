import pytest
from Test.object_instance import *

@pytest.mark.usefixtures("setup_scope_class")
class TestFooterUi(ObjectInstantiation):

    def test_precondition_step(self):
        self.login().admin_univ_already_login(1)
        print('Admin University Berhasil Login')

    def test_verify_theres_copyright(self):
        self.footer().check_copyright_is_visible()

    def test_verify_copyright_text_is_correct(self):
        self.footer().check_copyright_text_is_correct()

    def test_verify_theres_termsofuse(self):
        self.footer().check_terms_of_use_is_visible()

    def test_verify_termsofuse_text_indo_is_correct(self):
        self.navbar().change_language_to_indonesia()
        self.footer().check_terms_of_use_text_indo()

    def test_verify_termsofuse_text_english_is_correct(self):
        self.navbar().change_language_to_english()
        self.footer().check_terms_of_use_text_english()

    def test_verify_theres_privacypolicy(self):
        self.footer().check_privacy_policy_is_visible()

    def test_verify_privacypolicy_text_indo_is_correct(self):
        self.navbar().change_language_to_indonesia()
        self.footer().check_privacy_policy_text_indo()

    def test_verify_privacypolicy_text_english_is_correct(self):
        self.navbar().change_language_to_english()
        self.footer().check_privacy_policy_text_english()

@pytest.mark.usefixtures("setup_scope_class")
class TestFooterFunctionality(ObjectInstantiation):

    def test_precondition_step(self):
        self.login().admin_univ_already_login(1)
        print('Admin University Berhasil Login')

    def test_click_termsofuse_text(self):
        self.footer().click_terms_of_use()

    def test_click_privacy_text(self):
        self.footer().click_privacy_policy()


