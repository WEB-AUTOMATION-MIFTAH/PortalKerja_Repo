from selenium.webdriver.common.by import By

class LocatorLoginPage:

    """NAVBAR"""
    LOC_LOGO_POKER = (By.XPATH, '//a[@href="/"]/img')      # https://accel.id/static/media/homepage.16a45bfff1b9bd7c53961981fb422708.svg
    LOC_JOBS_NAV = (By.XPATH, '//a[@class="hn-menu-item active"]/h5')   # Pekerjaan | Jobs
    LOC_DEFAULT_FLAG = (By.XPATH, '//div[@class="flex-all-center"]/img')                # assert img default indonesia src=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAILSURBVHgBtZRPTxNBGMafmW5BjcYajBrlsBsPetRovPQgn8AS/QJ40XhQuJO4VOPdPxc8wRdAAT8AHOSA0cjJxFNXU6zaNrNImxY6u6/7jpJo2oVCt7/DZndn5nlm5v0jsAsFRRloTAilrsv1r7ZoNm0zoLUfXLi4JoaG5kOJBeeE8OI0RIywLTRmrMW5kYHFV0h9eNdxcXDlGrZv3ITO3ZqlFPKdjNoMCj9pwlpdcQ89nszIb+vohvDsOTQePvGDq9m8c0Y8jTUolGlqcPq5O/jyBQ7C1t37aNx5kD9/Wkzt/LPwz857EWf+rnUL38nfOYk5Ad+59Xbl45F7YxkkQH161g+y2cscE2lcApg7R0IcfjTJ2TfD79LsfmFurNuAdgNrpaMM5DSXMkSOUzFp0m9eR/WCcUlVNRqX571gvV+FUNURmfr86RL6hCgWbQnLSiy4bQZbTVuUfKJTm0X0gx903BSaJ4eHbfQBsQFfag0PfaKlsSZDgeVmC4nDmhRiXnAxHE1BnTyGRKlsArU6HPPhlWmppSkxWCtqnn9aBT9I43alDh8JUalFWgHy//3kdq3q1DOsEWmNd3T+UiW3FxMjXiZ31+PxSUobpPYTE54bFayK3XmbSYlsDlL5F1FjO16Yx3hOtOslXtNJS+xlJAeQE4TRtAVuiqZvEcHTAbyAsIwanjmOiE2Q33AzE0/WcWLAAAAAAElFTkSuQmCC
    LOC_LOGIN_NAV_BTN = (By.XPATH, '//div[@class="hn-right"]/div[3]/button/span')   # Login | Masuk
    LOC_SIGNUP_NAV_BTN = (By.XPATH, '//div[@class="hn-right"]/div[4]/button/span')  # Sign Up | Daftar

    LOC_FLAG_DROPDOWN = (By.XPATH, '//div[@class="flex-all-center"]')
    LOC_IND_OPT_FLAG = (By.XPATH, '//div[@id="hn-dropdown-lang"]/button[1]/img')    # data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAILSURBVHgBtZRPTxNBGMafmW5BjcYajBrlsBsPetRovPQgn8AS/QJ40XhQuJO4VOPdPxc8wRdAAT8AHOSA0cjJxFNXU6zaNrNImxY6u6/7jpJo2oVCt7/DZndn5nlm5v0jsAsFRRloTAilrsv1r7ZoNm0zoLUfXLi4JoaG5kOJBeeE8OI0RIywLTRmrMW5kYHFV0h9eNdxcXDlGrZv3ITO3ZqlFPKdjNoMCj9pwlpdcQ89nszIb+vohvDsOTQePvGDq9m8c0Y8jTUolGlqcPq5O/jyBQ7C1t37aNx5kD9/Wkzt/LPwz857EWf+rnUL38nfOYk5Ad+59Xbl45F7YxkkQH161g+y2cscE2lcApg7R0IcfjTJ2TfD79LsfmFurNuAdgNrpaMM5DSXMkSOUzFp0m9eR/WCcUlVNRqX571gvV+FUNURmfr86RL6hCgWbQnLSiy4bQZbTVuUfKJTm0X0gx903BSaJ4eHbfQBsQFfag0PfaKlsSZDgeVmC4nDmhRiXnAxHE1BnTyGRKlsArU6HPPhlWmppSkxWCtqnn9aBT9I43alDh8JUalFWgHy//3kdq3q1DOsEWmNd3T+UiW3FxMjXiZ31+PxSUobpPYTE54bFayK3XmbSYlsDlL5F1FjO16Yx3hOtOslXtNJS+xlJAeQE4TRtAVuiqZvEcHTAbyAsIwanjmOiE2Q33AzE0/WcWLAAAAAAElFTkSuQmCC
    LOC_IND_OPT_TXT = (By.XPATH, '//div[@id="hn-dropdown-lang"]/button[1]/div')         # Bahasa Indonesia
    LOC_ENG_OPT_FLAG = (By.XPATH, '//div[@id="hn-dropdown-lang"]/button[2]/img')    # data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAYCAYAAAAPtVbGAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAOmSURBVHgBtVZtTBxFGH7e+ygcQlxbQCKmrGIUoU1stTWNGMDGxPhRoBcTDWqLRk20kSNpzlg1x9WvYCTA6Q9+qCyNJv7xI6ZRf5h4kjbW9kcvV8pn21tS2hKOcgu99rjb605n90ra47iPNuFJZnZ29pn3eWfeeWeWkAGMMUENBndNPrG5iRETwUjU+wmkCO/s8SnPvuZ9+nH3gKz0yZnsmFbqrCpziNWlbf3tb34fIhP1MKB+ScAQBxMYUT2BdeRb1wR0rj4mZ5GqEsduk8aOc8O7CbnB4Gos8FCxw5FVpLrU0UHE+vkgIdGTq8x1YybWXcVtpBXx+081lZULrqSv2TSWfWfcuxdbtrqmPN2OFBEeYHHjxsru3wedePWtWhgLcAvQ2RUPFMPz/ma0yj/gytddrhFRFJNEZPtzrsXhIbGg0IYPPrFD+m0PH7QuZwn7zg345hkuJLmhDvmRV1sniH/90b/EIH0W0x87A8TdKWrZBdvDNcYqaJqG/w+PYUt1CQLbNqWYFt59D+aWtzEZmEH50YNgM9NcjpD36BYIO5r1ba7TGojIa+GN+rL9nTc5llgqExG21VYhPncxzQQIa9cVGQWPtS2fXKIiquMNL01sqPyVkakJ6aA7FImk9lutgNmCjIhr3gdHTjdYEI2KuB2oaqJkxiN6xQNPIlYPwnWR1YeJkaZg9WDYtpjvqfDhjgIxHUuPuzo+xp/JCWpey/OouASZwGKqDxNTsNz/z2Evf0+7u9SLs5BXyJOil19BSdteZIGPb2Poe3CAl574YgTKjwcQ/vOgEag1tXWYf6oZleV3phnPsDB/mZcI7l2vnw4ELRrFBfc+xKfOgXgyl357oFdn8pwjZfGETzr7kh2hzk9x9cJ5LNS9gI5jBfiu71BGN0NzYezc/iV+Gjikn38w5eWhbJ8b+TU1iBw5ItlsNtkQ0avpHc3t6vhJJb/RDm/jh3i99wwG/x5H1mOYhym8EMN+5894/snPcFYOwlxYiLudH6FiyO9eohki98myMr/3i3bn8Hp0dQ0ifGkRt4rAxCyat3+FTtcv+nHisNnukpNEdGx9o0XyH53sSHE180SSGFfCUUh9//KLj3pv5iUl4/Csx80YtfKmjJxwQ4YvrKIx5hid8biXs1IyfjTYI7EYNfA4SlmvLpaIGed6tRhtGgt6eleirXiMjio9Mn+0/vd5yM1UtZG3m/gfisjvCDHhP5PjoTnZYjV7KWaVRpSuSWTANaMfXV5w5NWrAAAAAElFTkSuQmCC
    LOC_ENG_OPT_TXT = (By.XPATH, '//div[@id="hn-dropdown-lang"]/button[2]/div')         # English


    """MODAL LOGIN"""
    LOC_EMAIL_FIELD = (By.XPATH, '//input[@id="login"]')
    LOC_PWD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOC_LOGIN_BTN = (By.XPATH, '//div[@class="modal-body"]/form/div[5]')
    LOC_TXT_TITLE_MDL = (By.XPATH, '//div[@class="modal-body"]/form/div/h4]')
    LOC_TXT_SUBTIT_MDL = (By.XPATH, '//div[@class="modal-body"]/form/div[1]/div/span')
    # assert txt : 'Silakan masuk dengan akun\natau akun'

    LOC_IMG_SUBTIT_1_MDL = (By.XPATH, '//div[@class="modal-body"]/form/div[1]/div/span/img[1]')
    # assert img 1 : https://accel.id/static/media/portal_sekolah_logo.953399c06435af1a4326b737e2ab70bd.svg

    LOC_IMG_SUBTIT_2_MDL = (By.XPATH, '//div[@class="modal-body"]/form/div[1]/div/span/img[2]')
    # assert img 2 : https://accel.id/static/media/portal_kerja_logo.735067de01e4d1d744a757f2a73f944a.svg
