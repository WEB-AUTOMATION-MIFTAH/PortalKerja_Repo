import pytest
from Test.object_instance import ObjectInstantiation

@pytest.mark.smoke
@pytest.mark.usefixtures("setup_scope_class")
class TestUIandCopywritingOfLandingPage(ObjectInstantiation):
    def test_tc_n001_there_is_logo(self):
        self.navbar().check_logo_is_exist()

    def test_tc_n002_there_is_nav_menu(self):
        self.navbar().check_nav_menu_jobs_is_exist()

    def test_tc_n003_nav_menu_in_two_language(self):
        self.navbar().check_nav_menu_jobs_in_two_languange()

    def test_tc_005_thereis_login_btn(self):
        self.navbar().check_login_btn_is_exist()

    def test_tc_006_ensure_login_btn_text_display_in_two_languages(self):
        self.navbar().check_login_btn_txt_in_two_language()

    def test_tc_007_thereis_signup_btn(self):
        self.navbar().check_login_btn_is_exist()

    def test_tc_008_ensure_signup_btn_text_display_in_two_languages(self):
        self.navbar().check_signup_btn_txt_in_two_language()

@pytest.mark.smoke
@pytest.mark.usefixtures("setup_scope_function")
class TestNavbarFunctionality(ObjectInstantiation):

    def test_tc_n004_default_language(self):
        self.navbar().check_default_selected_languange_is_indonesia()

    @pytest.mark.debug
    def test_tc_n009_dropdown_language_is_able_to_click(self):
        self.navbar().click_dropdown_language()
        self.navbar().check_option_list_indonesia_is_exist()
        self.navbar().check_option_list_english_is_exist()

    def test_tc_n010_login_btn_is_able_to_click(self):
        self.navbar().click_to_login_btn()
