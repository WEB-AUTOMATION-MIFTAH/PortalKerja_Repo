# import semua step module via > Test/__init__.py
from Test import *

class ObjectInstantiation:

    # Landing portal kerja
    def landingf(self):
        landingfunc = StepLandingFunc(self.driver)
        return landingfunc

    def landingui(self):
        landingui = StepLandingUI(self.driver)
        return landingui

    # Login portal kerja
    def loginf(self):
        login = StepLoginFunc(self.driver)
        return login

    def loginui(self):
        login = StepLoginUI(self.driver)
        return login

    # navbar hrms
    def navbarhrmsf(self):
        navf = StepHRMSDashboardFunc(self.driver)
        return navf




