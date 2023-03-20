import logging

from testselection.helper_for_tests import Helper
from testselection.group import Group

logger = logging.getLogger(__name__)

class TestGroup():
    def test_group_do_nothing(mocker):
        Helper.add_sleep(1)
        group = Group()
        assert group.return_true() == True

    def test_random_functionality(mocker):
        Helper.add_sleep(2)
        group = Group()
        assert group.random_functionality() == 1
