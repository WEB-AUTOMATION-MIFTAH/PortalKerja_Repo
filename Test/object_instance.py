from Stepdef.login_step_functionality import *
from Stepdef.login_step_ui_copywriting import *
from Stepdef.landingpage_step_ui_copywriting import *
from Stepdef.landingpage_step_functionality import *

class ObjectInstantiation:
    def login(self):
        login = StepDefLogin(self.driver)
        return login

    def navbar(self):
        navbar = StepLandingPage(self.driver)
        return navbar