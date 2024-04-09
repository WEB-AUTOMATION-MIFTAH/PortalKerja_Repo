from Config import dataconfig
from Pages.basemethod import CustomMethod
from Pages.privacypolicy import *

class StepDefPrivacyPolicyPage(CustomMethod, LocatorPrivacyPolicyAndTermsofUsePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_menu_kebijakan_privasi_is_visible(self):
        self.is_web_element_visible(self.LOC_MENU_KEBIJAKAN_PRIVASI)
        self.back_to_previous_page()

    def check_text_menu_kebijakan_privasi_is_correct(self):
        KebijakanPrivasi = self.get_text_of_element(self.LOC_MENU_KEBIJAKAN_PRIVASI)
        assert KebijakanPrivasi == 'Kebijakan Privasi', "Text Menu Tidak Sesuai"

    def check_menu_syaratketentuanpenggunaan_is_visible(self):
        self.is_web_element_visible(self.LOC_MENU_SYARAT_KETENTUAN_PENGGUNAAN)
        self.back_to_previous_page()

    def check_text_menu_syaratketentuanpenggunaan_is_correct(self):
        SyaratKetentuanPenggunaan = self.get_text_of_element(self.LOC_MENU_SYARAT_KETENTUAN_PENGGUNAAN)
        assert SyaratKetentuanPenggunaan == 'Syarat dan Ketentuan Penggunaan', "Text Menu Tidak Sesuai"