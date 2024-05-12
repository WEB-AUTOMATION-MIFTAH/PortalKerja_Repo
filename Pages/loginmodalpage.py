from selenium.webdriver.common.by import By

class LocLoginPage:
    LOC_MODAL_LOGIN = (By.XPATH, '//div[@class="modal-body"]')
    LOC_TXT_TITLE_MDL = (By.XPATH, '//div[@class="modal-body"]/form/div/h4]')
    LOC_TXT_SUBTIT_MDL = (By.XPATH, '//div[@class="modal-body"]/form/div[1]/div/span')  # assert txt : 'Silakan masuk dengan akun\natau akun'
    LOC_IMG_SUBTIT_1_MDL = (By.XPATH, '//div[@class="modal-body"]/form/div[1]/div/span/img[1]')  # assert img 1 : https://accel.id/static/media/portal_sekolah_logo.953399c06435af1a4326b737e2ab70bd.svg
    LOC_IMG_SUBTIT_2_MDL = (By.XPATH, '//div[@class="modal-body"]/form/div[1]/div/span/img[2]')  # assert img 2 : https://accel.id/static/media/portal_kerja_logo.735067de01e4d1d744a757f2a73f944a.svg
    LOC_EMAIL_FIELD = (By.XPATH, '//input[@id="login"]')
    LOC_PWD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOC_LOGIN_BTN = (By.XPATH, '//div[@class="modal-body"]/form/div[5]')
    LOC_FORGOT_PWD_LINKTXT = (By.XPATH, '//a[@href="/lupa-password"]')
    LOC_ERROR_MSG_LOGIN = (By.XPATH, "//div[@class='error-msg']")
    LOC_SIGNUP_FREE_NOW = (By.XPATH, '//a[@href="/select-role-registration"]')
