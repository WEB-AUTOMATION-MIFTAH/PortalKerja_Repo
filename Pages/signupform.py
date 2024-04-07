from selenium.webdriver.common.by import By


class LocatorSignupForm:
    LOC_1stNAME_LBL = '//div[@class="suc-form"]/div[1]/div/label'                 # Nama Depan | First Name
    LOC_1stNAME_LBL_MANDATORY = '//div[@class="suc-form"]/div[1]/div/span'        # *
    LOC_1stNAME = (By.XPATH, '//div[@class="suc-form"]/div[1]/div/div[1]/input')  # placeholder : Input First Name | Ketik Nama Depan

