from selenium.webdriver.common.by import By

class LocatorLoginPage:
    LOC_LOGIN_NAV_BTN = (By.XPATH, '//div[@class="hn-right"]/div[3]')
    LOC_EMAIL_FIELD = (By.XPATH, '//input[@id="login"]')
    LOC_PWD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOC_LOGIN_BTN = (By.XPATH, '//div[@class="modal-body"]/form/div[5]')

    LOC_TXT_TITLE_MDL = (By.XPATH, '//div[@class="modal-body"]/form/div/h4]')
    LOC_TXT_SUBTIT_1_MDL = (By.XPATH, '//div[@class="modal-body"]/form/div[1]/div/span/text()[1]')
    LOC_TXT_SUBTIT_2_MDL = (By.XPATH, '//div[@class="modal-body"]/form/div[1]/div/span/text()[2]')
    LOC_IMG_SUBTIT_1_MDL = (By.XPATH, '//div[@class="modal-body"]/form/div[1]/div/span/img[1]')
    LOC_IMG_SUBTIT_2_MDL = (By.XPATH, '//div[@class="modal-body"]/form/div[1]/div/span/img[2]')

