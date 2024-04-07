from Config.dataconfig import TestData
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # for chrome only
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")  # for chrome only
options.add_argument("--start-maximized")
options.add_argument('--log-level=3')
# options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get(TestData.BASE_URL_STAGING)
driver.find_element(By.XPATH, '//div[@class="hn-right"]/div[3]').click()
src_ = driver.find_element(By.XPATH, '//div[@class="modal-body"]/form/div[1]/div/span/img[1]').get_attribute(name="src")

driver.quit()




