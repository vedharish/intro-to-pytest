import logging

from testselection.helper_for_tests import Helper
from testselection.group import Group

logger = logging.getLogger(__name__)

class TestGroup():
    def test_group_do_nothing(mocker):
        Helper.add_sleep(1)
        group = Group()
        assert group.return_true() == True
