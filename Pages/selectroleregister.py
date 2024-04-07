from selenium.webdriver.common.by import By

class LocatorSelectRoleReg:

    LOC_LOGO_POKER = (By.XPATH, '//div[@class="modules-select"]/img')      # https://accel.id/static/media/portal-kerja.83001e8cded50a51024c.png
    LOC_TITLE = (By.XPATH, '//div[@class="modules-select"]/p')   # Which role that you want to register? | Role apa yang Anda ingin daftar?
    LOC_SELECTION_BOXS = (By.XPATH, '//div[@class="modules-select"]/div/div') # plurals check langsung 2 box is exist!
    LOC_SVG_ICONS = (By.CSS_SELECTOR, 'div.main-wrapper>div>div>div>div>svg:nth-of-type(1)')    # plurals check langsung 2 svg is exist!
    LOC_CANDIDATE_TXT = (By.XPATH, '//div[@class="modules-select"]/div/div[1]/p')   # Kandidat | Candidate
    LOC_EMPLOYER_TXT = (By.XPATH, '//div[@class="modules-select"]/div/div[2]/p')    # Perusahaan | Employer

