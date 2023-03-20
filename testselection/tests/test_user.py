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

    def test_addition_odd(mocker):
        Helper.add_sleep(0.2)
        user = User()
        assert 4 == user.add_two_numbers(1, 3)

    def test_addition_even(mocker):
        Helper.add_sleep(1.2)
        user = User()
        assert 6 == user.add_two_numbers(2, 4)

    def test_substraction_even(mocker):
        Helper.add_sleep(2)
        user = User()
        assert 18 == user.substract_two_numbers(20, 2)

    def test_substraction_odd(mocker):
        Helper.add_sleep(1.1)
        user = User()
        assert 18 == user.add_two_numbers(19, 1)
