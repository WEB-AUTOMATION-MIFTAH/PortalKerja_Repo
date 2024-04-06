from Config import dataconfig
from Pages.basemethod import CustomMethod
from Pages.dashboard import LocatorNavbar

class StepDefNavbarAllRole(CustomMethod, LocatorNavbar):

    def __init__(self, driver):
        super().__init__(driver)

    def click_dropdown_language_nav(self):
        self.click_to(self.LOC_DROPDOWN_LANGUAGE)
        self.is_visible(self.LOC_SELECT_IN)
        self.is_visible(self.LOC_SELECT_IN)

    def check_text_at_indonesia_flag(self):
        self.click_to(self.LOC_DROPDOWN_LANGUAGE)
        ID_text = self.get_element_text(self.LOC_SELECT_IN)
        assert ID_text == 'ID', 'text ID tidak sesuai'

    def check_text_at_english_flag(self):
        self.click_to(self.LOC_DROPDOWN_LANGUAGE)
        EN_text = self.get_element_text(self.LOC_SELECT_EN)
        assert EN_text == 'EN', 'text EN tidak sesuai'

    def change_language_to_english(self):
        self.click_to(self.LOC_DROPDOWN_LANGUAGE)
        self.click_to(self.LOC_SELECT_EN)
        self.is_visible(self.LOC_SELECTED_LANGUAGE_EN)

    def change_language_to_indonesia(self):
        self.click_to(self.LOC_DROPDOWN_LANGUAGE)
        self.click_to(self.LOC_SELECT_IN)
        self.is_visible(self.LOC_SELECTED_LANGUAGE_ID)

    def click_dropdown_profile_nav(self):
        self.click_to(self.LOC_DROPDOWN_NAVBAR_PROFILE)

    def check_profile_setting_is_visible(self):
        self.click_to(self.LOC_DROPDOWN_NAVBAR_PROFILE)
        self.is_visible(self.LOC_SETTING_PROFILE)

    def check_copywriting_profile_setting_text(self):
        self.change_language_to_english()
        self.click_dropdown_profile_nav()
        profile_setting_eng = self.get_element_text(self.LOC_SETTING_PROFILE)
        assert profile_setting_eng == 'Profile Setting'
        self.change_language_to_indonesia()
        self.click_dropdown_profile_nav()
        profile_setting_ind = self.get_element_text(self.LOC_SETTING_PROFILE)
        assert profile_setting_ind == 'Pengaturan Profile'

    def check_help_center_is_visible(self):
        self.click_to(self.LOC_DROPDOWN_NAVBAR_PROFILE)
        self.is_visible(self.LOC_HELPCENTER)

    def check_copywriting_helpcenter_text(self):
        pass

    def check_logout_is_visible(self):
        self.click_to(self.LOC_DROPDOWN_NAVBAR_PROFILE)
        self.is_visible(self.LOC_LOGOUT)

    def check_copywriting_logout_text(self):
        pass


'''-------------------------------------------------------------------------------------------'''

class StepDefNavbarAdminOrLecturer(StepDefNavbarAllRole):

    pass

'''-------------------------------------------------------------------------------------------'''

class StepDefNavbarStudent(StepDefNavbarAllRole):

    pass












