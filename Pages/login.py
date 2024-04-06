from selenium.webdriver.common.by import By

class LocatorLoginPage:
    LOC_LOGIN_NAV_BTN = (By.XPATH, '//div[@class="hn-right"]/div[3]')
    LOC_EMAIL_FIELD = (By.XPATH, '//input[@id="login"]')
    LOC_PWD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOC_LOGIN_BTN = (By.XPATH, '//div[@class="modal-body"]/form/div[5]')
