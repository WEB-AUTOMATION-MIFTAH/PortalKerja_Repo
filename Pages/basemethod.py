import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all Pages It contains custom methods for all the pages"""

class CustomMethod:

    def __init__(self, driver):
        self.driver = driver

    def click_to(self, locator):
        if isinstance(locator, tuple):
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).click()
        elif isinstance(locator, WebElement):
            locator.click()
        else:
            raise ValueError("Invalid input. harus masukin tuple(locator) atau WebElement ya bro!!!")

    def fill_in(self, locator, input_text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).send_keys(input_text)

    def clear_field(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).clear()

    def is_web_element_visible(self, locator):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(locator))
        return bool(element)

    # return objek instance dari kelas WebElement
    def get_web_element(self, locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return element

    def get_attr_element(self, locator, attrib):
        attribute = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).get_attribute(attrib)
        return attribute

    def get_text_of_element(self, locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return element.text

    def get_list_all_elements(self, locators):
        elements_lists = WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(locators))
        return elements_lists

    def drag_and_drop(self, input_source_locator, input_target_locator):
        actions = ActionChains(self.driver)
        source = self.get_web_element(input_source_locator)
        target = self.get_web_element(input_target_locator)
        actions.drag_and_drop(source, target).perform()

    def switch_to_frame(self, locator):
        WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def switch_to_default_frame(self):
        self.driver.switch_to.default_content()

    def accept_alert_js(self):
        alert_msg = self.driver.switch_to.alert
        alert_msg.accept()

    def enter_keyboard(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def back_to_previous_page(self):
        self.driver.back()

    def forward_to_next_page(self):
        self.driver.forward()

    def get_length_all_elements(self, locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(locator))
        return len(element)

    def move_to_element(self, locators):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_web_element(locators)).perform()
        time.sleep(1.5)

    def scroll_down_page(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

    def scroll_up_page(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_UP)
        actions.perform()