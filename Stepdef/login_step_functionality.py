from Pages.basemethod import CustomMethod
from Pages.loginmodalpage import LocLoginPage

class StepLoginFunc(CustomMethod, LocLoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    def login_with_user_credential(self, email, password):
        self.fill_in(self.LOC_EMAIL_FIELD, email)
        self.fill_in(self.LOC_PWD_FIELD, password)
        self.click_to(self.LOC_LOGIN_BTN)

    def login_as_super_admin(self):
        pass

    def login_as_jobseeker_only(self):
        pass

    def login_as_admin_default(self):
        pass

    def login_as_admin_custom_all_module_viewonly(self):
        pass

    def login_as_admin_custom_all_module_fullaccess(self):
        pass

    def login_as_employee_default(self):
        pass

    def login_as_admin_default_child_company_first_register(self):
        print("Expected cannot access HRMS")
        pass

    def login_as_admin_custom_child_company(self):
        pass