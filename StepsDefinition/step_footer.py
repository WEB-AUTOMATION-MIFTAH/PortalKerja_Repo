# from Config import dataconfig
# from Pages.basemethod import CustomMethod
# from Pages.dashboard import LocatorFooter
#
# class StepDefFooter(LocatorFooter, CustomMethod):
#
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     def check_copyright_is_visible(self):
#         self.is_web_element_visible(self.LOC_COPYRIGHT_TXT)
#
#     def check_copyright_text_is_correct(self):
#         text_copyright = self.get_text_of_element(self.LOC_COPYRIGHT_TXT)
#         assert text_copyright == "Copyright © 2024 Portal Kampus. All right reserved."
#     '''-----------------------------------------------------------------------------------------------'''
#     def check_terms_of_use_is_visible(self):
#         self.is_web_element_visible(self.LOC_TERMOFUSE_TXT)
#
#     def check_terms_of_use_text_indo(self):
#         txt_termsofuse = self.get_text_of_element(self.LOC_TERMOFUSE_TXT)
#         assert txt_termsofuse == "Syarat Ketentuan Penggunaan"
#
#     def check_terms_of_use_text_english(self):
#         txt_termsofuse = self.get_text_of_element(self.LOC_TERMOFUSE_TXT)
#         assert txt_termsofuse == "Terms of Use"
#
#     def click_terms_of_use(self):
#         self.click_to(self.LOC_TERMOFUSE_TXT)
#         self.check_menu_syaratketentuanpenggunaan_is_visible()
#
#     '''-----------------------------------------------------------------------------------------------'''
#     def check_privacy_policy_is_visible(self):
#         self.is_web_element_visible(self.LOC_PRIVACYPOLCY_TXT)
#
#     def check_privacy_policy_text_indo(self):
#         txt_privacy = self.get_text_of_element(self.LOC_PRIVACYPOLCY_TXT)
#         assert txt_privacy == "Kebijakan Privasi"
#
#     def check_privacy_policy_text_english(self):
#         txt_privacy = self.get_text_of_element(self.LOC_PRIVACYPOLCY_TXT)
#         assert txt_privacy == "Privacy Policy"
#
#     def click_privacy_policy(self):
#         self.click_to(self.LOC_PRIVACYPOLCY_TXT)
#         self.check_menu_kebijakan_privasi_is_visible()
#
#
#
#
#
#
#
#
#
#
#
#
