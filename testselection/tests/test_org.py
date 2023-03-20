import logging

from testselection.helper_for_tests import Helper
from testselection.org import Org

logger = logging.getLogger(__name__)

class TestUser():
    def test_balance(mocker):
        Helper.add_sleep(1)
        org = Org(200)
        assert 200 == org.get_balance()

    def test_deposit(mocker):
        Helper.add_sleep(1)
        org = Org(200)
        org.deposit_money(100)
        assert 300 == org.get_balance()

    def test_withdraw(mocker):
        Helper.add_sleep(1)
        org = Org(200)
        org.withdraw_money(100)
        assert 100 == org.get_balance()
