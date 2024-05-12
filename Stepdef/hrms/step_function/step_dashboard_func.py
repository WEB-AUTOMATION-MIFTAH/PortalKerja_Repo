from Pages.basemethod import CustomMethod
from Pages.hrms.hrmsdashboardpage import LocHRMSDashboardPage

class StepHRMSDashboardFunc(CustomMethod, LocHRMSDashboardPage):

    def __init__(self, driver):
        super().__init__(driver)

    # NAVBAR SECTION
    def check_role_name_in_navbar_is_superadmin(self):
        a = self.get_text_of_element(self.LOC_ROLE_NAME_IN_NAVBAR)
        assert a == "Super Admin", "Role Name is Unexpected!!!"