import pytest
from Test.object_instance import ObjectInstantiation

@pytest.mark.usefixtures("setup_scope_class")
class TestFooterUi(ObjectInstantiation):

    @pytest.mark.smoke
    def test_verify_theres_copyright(self):
        self.footer().check_copyright_is_visible()