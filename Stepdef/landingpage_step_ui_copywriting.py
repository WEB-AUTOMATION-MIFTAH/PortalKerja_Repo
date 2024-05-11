from Stepdef.landingpage_step_functionality import StepLandingFunc

class StepLandingUI(StepLandingFunc):

    def __init__(self, driver):
        super().__init__(driver)

    # NAVBAR SECTION
    def check_logo_is_exist(self):
        a = self.is_web_element_visible(self.LOC_LOGO_POKER)
        assert a, "logo is not exist"

    def check_copywriting_of_jobs_menu_on_the_navbar(self):
        self.change_language_to_indonesia()
        txt_ind = self.get_text_of_element(self.LOC_JOBS_NAV)
        assert txt_ind == 'Pekerjaan', 'Copywriting-Indonesia tidak sesuai'
        self.change_language_to_english()
        txt_eng = self.get_text_of_element(self.LOC_JOBS_NAV)
        assert txt_eng == 'Jobs', 'Copywriting-English tidak sesuai'

    def check_copywriting_of_login_btn_on_the_navbar(self):
        self.change_language_to_indonesia()
        txt_ind = self.get_text_of_element(self.LOC_LOGIN_BTN)
        assert txt_ind == 'Masuk', 'Copywriting indonesia is not correct'
        self.change_language_to_english()
        txt_eng = self.get_text_of_element(self.LOC_LOGIN_BTN)
        assert txt_eng == 'Login', 'Copywriting englisg is not correct'

    def check_copywriting_of_signup_btn_on_the_navbar(self):
        self.change_language_to_indonesia()
        txt_ind = self.get_text_of_element(self.LOC_SIGNUP_BTN)
        assert txt_ind == 'Daftar', 'Copywriting indonesia is not correct'
        self.change_language_to_english()
        txt_eng = self.get_text_of_element(self.LOC_SIGNUP_BTN)
        assert txt_eng == 'Sign Up', 'Copywriting englisg is not correct'

    # BODY SECTION


    # FOOTER SECTION
    def check_site_link_teks_on_the_footer(self):
        sitelink = self.is_web_element_visible(self.LOC_SITELINKS_TXT)
        assert sitelink

