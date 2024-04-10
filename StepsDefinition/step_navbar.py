from Config import dataconfig
from Pages.basemethod import CustomMethod
from Pages.dashboard import LocatorNavbar
from Pages.login import LocatorLoginModal
from Pages.selectroleregister import LocatorSelectRoleReg

class StepdefNavbarDefault(CustomMethod, LocatorNavbar, LocatorLoginModal, LocatorSelectRoleReg):

    def __init__(self, driver):
        super().__init__(driver)

    def check_logo_is_exist(self):
        self.is_web_element_visible(self.LOC_LOGO_POKER)

    def check_default_selected_languange_is_indonesia(self):
        attribute = self.get_attr_element(self.LOC_SELECTED_FLAG, 'src')
        assert attribute == 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAILSURBVHgBtZRPTxNBGMafmW5BjcYajBrlsBsPetRovPQgn8AS/QJ40XhQuJO4VOPdPxc8wRdAAT8AHOSA0cjJxFNXU6zaNrNImxY6u6/7jpJo2oVCt7/DZndn5nlm5v0jsAsFRRloTAilrsv1r7ZoNm0zoLUfXLi4JoaG5kOJBeeE8OI0RIywLTRmrMW5kYHFV0h9eNdxcXDlGrZv3ITO3ZqlFPKdjNoMCj9pwlpdcQ89nszIb+vohvDsOTQePvGDq9m8c0Y8jTUolGlqcPq5O/jyBQ7C1t37aNx5kD9/Wkzt/LPwz857EWf+rnUL38nfOYk5Ad+59Xbl45F7YxkkQH161g+y2cscE2lcApg7R0IcfjTJ2TfD79LsfmFurNuAdgNrpaMM5DSXMkSOUzFp0m9eR/WCcUlVNRqX571gvV+FUNURmfr86RL6hCgWbQnLSiy4bQZbTVuUfKJTm0X0gx903BSaJ4eHbfQBsQFfag0PfaKlsSZDgeVmC4nDmhRiXnAxHE1BnTyGRKlsArU6HPPhlWmppSkxWCtqnn9aBT9I43alDh8JUalFWgHy//3kdq3q1DOsEWmNd3T+UiW3FxMjXiZ31+PxSUobpPYTE54bFayK3XmbSYlsDlL5F1FjO16Yx3hOtOslXtNJS+xlJAeQE4TRtAVuiqZvEcHTAbyAsIwanjmOiE2Q33AzE0/WcWLAAAAAAElFTkSuQmCC', 'Default language image selection not corect!!'

    def check_selected_languange_is_english(self):
        attribute = self.get_attr_element(self.LOC_SELECTED_FLAG, 'src')
        assert attribute == 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAYCAYAAAAPtVbGAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAOmSURBVHgBtVZtTBxFGH7e+ygcQlxbQCKmrGIUoU1stTWNGMDGxPhRoBcTDWqLRk20kSNpzlg1x9WvYCTA6Q9+qCyNJv7xI6ZRf5h4kjbW9kcvV8pn21tS2hKOcgu99rjb605n90ra47iPNuFJZnZ29pn3eWfeeWeWkAGMMUENBndNPrG5iRETwUjU+wmkCO/s8SnPvuZ9+nH3gKz0yZnsmFbqrCpziNWlbf3tb34fIhP1MKB+ScAQBxMYUT2BdeRb1wR0rj4mZ5GqEsduk8aOc8O7CbnB4Gos8FCxw5FVpLrU0UHE+vkgIdGTq8x1YybWXcVtpBXx+081lZULrqSv2TSWfWfcuxdbtrqmPN2OFBEeYHHjxsru3wedePWtWhgLcAvQ2RUPFMPz/ma0yj/gytddrhFRFJNEZPtzrsXhIbGg0IYPPrFD+m0PH7QuZwn7zg345hkuJLmhDvmRV1sniH/90b/EIH0W0x87A8TdKWrZBdvDNcYqaJqG/w+PYUt1CQLbNqWYFt59D+aWtzEZmEH50YNgM9NcjpD36BYIO5r1ba7TGojIa+GN+rL9nTc5llgqExG21VYhPncxzQQIa9cVGQWPtS2fXKIiquMNL01sqPyVkakJ6aA7FImk9lutgNmCjIhr3gdHTjdYEI2KuB2oaqJkxiN6xQNPIlYPwnWR1YeJkaZg9WDYtpjvqfDhjgIxHUuPuzo+xp/JCWpey/OouASZwGKqDxNTsNz/z2Evf0+7u9SLs5BXyJOil19BSdteZIGPb2Poe3CAl574YgTKjwcQ/vOgEag1tXWYf6oZleV3phnPsDB/mZcI7l2vnw4ELRrFBfc+xKfOgXgyl357oFdn8pwjZfGETzr7kh2hzk9x9cJ5LNS9gI5jBfiu71BGN0NzYezc/iV+Gjikn38w5eWhbJ8b+TU1iBw5ItlsNtkQ0avpHc3t6vhJJb/RDm/jh3i99wwG/x5H1mOYhym8EMN+5894/snPcFYOwlxYiLudH6FiyO9eohki98myMr/3i3bn8Hp0dQ0ifGkRt4rAxCyat3+FTtcv+nHisNnukpNEdGx9o0XyH53sSHE180SSGFfCUUh9//KLj3pv5iUl4/Csx80YtfKmjJxwQ4YvrKIx5hid8biXs1IyfjTYI7EYNfA4SlmvLpaIGed6tRhtGgt6eleirXiMjio9Mn+0/vd5yM1UtZG3m/gfisjvCDHhP5PjoTnZYjV7KWaVRpSuSWTANaMfXV5w5NWrAAAAAElFTkSuQmCC'

    def check_nav_menu_jobs_is_exist(self):
        self.is_web_element_visible(self.LOC_JOBS_NAV)

    def check_nav_menu_jobs_in_two_languange(self):
        self.change_language_to_indonesia()
        txt_ind = self.get_text_of_element(self.LOC_JOBS_NAV)
        assert txt_ind == 'Pekerjaan', 'Copywriting-Indonesia tidak sesuai'
        self.change_language_to_english()
        txt_eng = self.get_text_of_element(self.LOC_JOBS_NAV)
        assert txt_eng == 'Jobs', 'Copywriting-English tidak sesuai'

    def click_dropdown_language(self):
        self.click_to(self.LOC_FLAG_DROPDOWN)

    def change_language_to_english(self):
        self.click_to(self.LOC_FLAG_DROPDOWN)
        self.click_to(self.LOC_ENG_OPT_FLAG)
        self.check_selected_languange_is_english()

    def change_language_to_indonesia(self):
        self.click_to(self.LOC_FLAG_DROPDOWN)
        self.click_to(self.LOC_IND_OPT_FLAG)
        self.check_default_selected_languange_is_indonesia()

    def check_option_list_indonesia_is_exist(self):
        attr = self.get_attr_element(self.LOC_IND_OPT_FLAG, 'src')
        assert attr == 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAILSURBVHgBtZRPTxNBGMafmW5BjcYajBrlsBsPetRovPQgn8AS/QJ40XhQuJO4VOPdPxc8wRdAAT8AHOSA0cjJxFNXU6zaNrNImxY6u6/7jpJo2oVCt7/DZndn5nlm5v0jsAsFRRloTAilrsv1r7ZoNm0zoLUfXLi4JoaG5kOJBeeE8OI0RIywLTRmrMW5kYHFV0h9eNdxcXDlGrZv3ITO3ZqlFPKdjNoMCj9pwlpdcQ89nszIb+vohvDsOTQePvGDq9m8c0Y8jTUolGlqcPq5O/jyBQ7C1t37aNx5kD9/Wkzt/LPwz857EWf+rnUL38nfOYk5Ad+59Xbl45F7YxkkQH161g+y2cscE2lcApg7R0IcfjTJ2TfD79LsfmFurNuAdgNrpaMM5DSXMkSOUzFp0m9eR/WCcUlVNRqX571gvV+FUNURmfr86RL6hCgWbQnLSiy4bQZbTVuUfKJTm0X0gx903BSaJ4eHbfQBsQFfag0PfaKlsSZDgeVmC4nDmhRiXnAxHE1BnTyGRKlsArU6HPPhlWmppSkxWCtqnn9aBT9I43alDh8JUalFWgHy//3kdq3q1DOsEWmNd3T+UiW3FxMjXiZ31+PxSUobpPYTE54bFayK3XmbSYlsDlL5F1FjO16Yx3hOtOslXtNJS+xlJAeQE4TRtAVuiqZvEcHTAbyAsIwanjmOiE2Q33AzE0/WcWLAAAAAAElFTkSuQmCC', 'Option List Indonesia Tdk ada!'
        txt_opt_ind = self.get_text_of_element(self.LOC_IND_OPT_TXT)
        assert txt_opt_ind == 'Bahasa Indonesia', 'text pilihan bahasa indonesia tidak ada'

    def check_option_list_english_is_exist(self):
        attr = self.get_attr_element(self.LOC_ENG_OPT_FLAG, 'src')
        assert attr == 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAYCAYAAAAPtVbGAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAOmSURBVHgBtVZtTBxFGH7e+ygcQlxbQCKmrGIUoU1stTWNGMDGxPhRoBcTDWqLRk20kSNpzlg1x9WvYCTA6Q9+qCyNJv7xI6ZRf5h4kjbW9kcvV8pn21tS2hKOcgu99rjb605n90ra47iPNuFJZnZ29pn3eWfeeWeWkAGMMUENBndNPrG5iRETwUjU+wmkCO/s8SnPvuZ9+nH3gKz0yZnsmFbqrCpziNWlbf3tb34fIhP1MKB+ScAQBxMYUT2BdeRb1wR0rj4mZ5GqEsduk8aOc8O7CbnB4Gos8FCxw5FVpLrU0UHE+vkgIdGTq8x1YybWXcVtpBXx+081lZULrqSv2TSWfWfcuxdbtrqmPN2OFBEeYHHjxsru3wedePWtWhgLcAvQ2RUPFMPz/ma0yj/gytddrhFRFJNEZPtzrsXhIbGg0IYPPrFD+m0PH7QuZwn7zg345hkuJLmhDvmRV1sniH/90b/EIH0W0x87A8TdKWrZBdvDNcYqaJqG/w+PYUt1CQLbNqWYFt59D+aWtzEZmEH50YNgM9NcjpD36BYIO5r1ba7TGojIa+GN+rL9nTc5llgqExG21VYhPncxzQQIa9cVGQWPtS2fXKIiquMNL01sqPyVkakJ6aA7FImk9lutgNmCjIhr3gdHTjdYEI2KuB2oaqJkxiN6xQNPIlYPwnWR1YeJkaZg9WDYtpjvqfDhjgIxHUuPuzo+xp/JCWpey/OouASZwGKqDxNTsNz/z2Evf0+7u9SLs5BXyJOil19BSdteZIGPb2Poe3CAl574YgTKjwcQ/vOgEag1tXWYf6oZleV3phnPsDB/mZcI7l2vnw4ELRrFBfc+xKfOgXgyl357oFdn8pwjZfGETzr7kh2hzk9x9cJ5LNS9gI5jBfiu71BGN0NzYezc/iV+Gjikn38w5eWhbJ8b+TU1iBw5ItlsNtkQ0avpHc3t6vhJJb/RDm/jh3i99wwG/x5H1mOYhym8EMN+5894/snPcFYOwlxYiLudH6FiyO9eohki98myMr/3i3bn8Hp0dQ0ifGkRt4rAxCyat3+FTtcv+nHisNnukpNEdGx9o0XyH53sSHE180SSGFfCUUh9//KLj3pv5iUl4/Csx80YtfKmjJxwQ4YvrKIx5hid8biXs1IyfjTYI7EYNfA4SlmvLpaIGed6tRhtGgt6eleirXiMjio9Mn+0/vd5yM1UtZG3m/gfisjvCDHhP5PjoTnZYjV7KWaVRpSuSWTANaMfXV5w5NWrAAAAAElFTkSuQmCC', 'Option List English Tdk ada!'
        txt_opt_eng = self.get_text_of_element(self.LOC_ENG_OPT_TXT)
        assert txt_opt_eng == 'English', 'text pilihan bahasa inggris tidak ada'

    def check_login_btn_is_exist(self):
        self.is_web_element_visible(self.LOC_LOGIN_BTN)

    def check_login_btn_txt_in_two_language(self):
        self.change_language_to_indonesia()
        txt_ind = self.get_text_of_element(self.LOC_LOGIN_BTN)
        assert txt_ind == 'Masuk', 'Copywriting indonesia is not correct'
        self.change_language_to_english()
        txt_eng = self.get_text_of_element(self.LOC_LOGIN_BTN)
        assert txt_eng == 'Login', 'Copywriting englisg is not correct'

    def check_signup_btn_is_exist(self):
        self.is_web_element_visible(self.LOC_SIGNUP_BTN)

    def check_signup_btn_txt_in_two_language(self):
        self.change_language_to_indonesia()
        txt_ind = self.get_text_of_element(self.LOC_SIGNUP_BTN)
        assert txt_ind == 'Daftar', 'Copywriting indonesia is not correct'
        self.change_language_to_english()
        txt_eng = self.get_text_of_element(self.LOC_SIGNUP_BTN)
        assert txt_eng == 'Sign Up', 'Copywriting englisg is not correct'

    def click_to_login_btn(self):
        self.click_to(self.LOC_LOGIN_BTN)
        self.is_web_element_visible(self.LOC_MODAL_LOGIN)

    def click_to_signup_btn(self):
        self.click_to(self.LOC_SIGNUP_BTN)
        self.is_web_element_visible(self.LOC_TITLE)



