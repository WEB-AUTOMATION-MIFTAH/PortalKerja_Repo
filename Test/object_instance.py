from StepsDefinition.step_navbar import StepdefNavbarDefault
from StepsDefinition.step_login import *

class ObjectInstantiation:
    def login(self):
        login = StepDefLogin(self.driver)
        return login

    def navbar(self):
        navbar = StepdefNavbarDefault(self.driver)
        return navbar

    def footer(self):
        footer = StepDefFooter(self.driver)
        return footer

    def privacy(self):
        privacy = StepDefPrivacyPolicyPage(self.driver)
        return privacy