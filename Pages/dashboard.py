from selenium.webdriver.common.by import By


class LocatorNavbar:
    LOC_DROPDOWN_LANGUAGE = (By.XPATH, "")
    LOC_SELECT_IN = (By.XPATH, "")
    LOC_SELECT_EN = (By.XPATH, "")
    # Note utk locator dibawah -> assert contains : indonesia_flag | english_flag
    LOC_SELECTED_LANGUAGE_ID = (By.XPATH, "//button[contains(@class, 'joy-10m9115')]/img[contains(@srcset, 'indonesia_flag')]")
    LOC_SELECTED_LANGUAGE_EN = (By.XPATH, "//button[contains(@class, 'joy-10m9115')]/img[contains(@srcset, 'english_flag')]")

    LOC_PROFILE_NAME = (By.XPATH, "")
    LOC_ROLE_NAME = (By.XPATH, "")
    LOC_DROPDOWN_NAVBAR_PROFILE = (By.XPATH, "")
    LOC_SETTING_PROFILE = (By.XPATH, "")
    LOC_HELPCENTER = (By.XPATH, "")
    LOC_LOGOUT = (By.XPATH, "")

class LocatorSidebarHRMS:
    pass

class LocatorMainContentHRMS:
    pass

class LocatorSidebarJobseeker:
    pass

class LocatorMainContentJobseeker:
    pass

class LocatorSidebarJobPoster:
    pass

class LocatorMainContentJobPoster:
    pass

class LocatorFooter:
    LOC_COPYRIGHT_TXT = (By.XPATH, '')
    LOC_TERMOFUSE_TXT = (By.XPATH, "")
    LOC_PRIVACYPOLCY_TXT = (By.XPATH, "")
