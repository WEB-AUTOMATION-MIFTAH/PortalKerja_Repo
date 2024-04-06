from StepsDefinition.step_footer import StepDefFooter
from StepsDefinition.step_navbar import StepDefNavbarAllRole
from StepsDefinition.step_login import StepDefLogin
from StepsDefinition.step_privacy_termsofuse import *
from StepsDefinition.step_login import *

class ObjectInstantiation:
    def login(self):
        login = StepDefLogin(self.driver)
        return login

    def navbar(self):
        navbar = StepDefNavbarAllRole(self.driver)
        return navbar

    def footer(self):
        footer = StepDefFooter(self.driver)
        return footer

    def privacy(self):
        privacy = StepDefPrivacyPolicyPage(self.driver)
        return privacy