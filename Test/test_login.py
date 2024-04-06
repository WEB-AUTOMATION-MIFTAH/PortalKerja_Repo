import pytest
from Test.object_instance import ObjectInstantiation

@pytest.mark.usefixtures("setup_scope_class")
class TestLogin(ObjectInstantiation):

    @pytest.mark.smoke
    def test_login_superadmin(self):
        self.login().user_do_login('visiprimaqa+27@gmail.com', 'Password123*')