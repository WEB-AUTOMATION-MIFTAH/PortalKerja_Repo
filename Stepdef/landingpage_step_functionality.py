from Pages.basemethod import CustomMethod
from Pages.landingpage import *

class StepLandingPage(CustomMethod, LocNavbarLandingPage, LocBodyLandingPage, LocFooterLandingPage):

    def __init__(self, driver):
        super().__init__(driver)

    '''Navbar Section'''
    def click_to_logo_navbar(self):
        pass

    def click_to_jobs_menu(self):
        pass

    def click_to_login_button(self):
        pass

    def click_to_signup_button(self):
        pass

    '''Body Section'''
    def input_searchbar_jobtitle_company(self):
        pass

    def input_searchbar_area(self):
        pass

    def click_to_find_job_button(self):
        pass

    '''Footer Section'''
    def click_to_facebook_icon(self):
        pass

    def click_to_instagram_icon(self):
        pass

    def click_to_youtube_icon(self):
        pass

    def click_to_tiktok_icon(self):
        pass

    def click_to_jobs_site_links(self):
        pass

    def click_to_company_site_links(self):
        pass

    def click_to_company_privacy_policy_links(self):
        pass

    def click_to_terms_and_condition_site_links(self):
        pass

