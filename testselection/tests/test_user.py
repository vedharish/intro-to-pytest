import logging

from testselection.helper_for_tests import Helper
from testselection.user import User

logger = logging.getLogger(__name__)

class TestUser():
    def test_addition(mocker):
        Helper.add_sleep(1)
        user = User()
        assert 2 == user.add_two_numbers(1, 1)

    def test_addition_again(mocker):
        Helper.add_sleep(0.8)
        user = User()
        assert 9 == user.add_two_numbers(4, 5)
