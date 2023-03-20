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
        Helper.add_sleep(0.4)
        org = Org(200)
        org.deposit_money(100)
        assert 300 == org.get_balance()

    def test_withdraw(mocker):
        Helper.add_sleep(0.6)
        org = Org(200)
        org.withdraw_money(100)
        assert 100 == org.get_balance()

    def test_custom_1(mocker):
        Helper.add_sleep(1.2)
        org = Org(200)
        org.deposit_money(100)
        org.withdraw_money(100)
        assert 200 == org.get_balance()

    def test_custom_2(mocker):
        Helper.add_sleep(2.2)
        org = Org(200)
        org.withdraw_money(100)
        org.deposit_money(100)
        assert 200 == org.get_balance()

    def test_custom_3(mocker):
        Helper.add_sleep(0.2)
        org = Org(200)
        org.withdraw_money(100)
        org.withdraw_money(100)
        assert 0 == org.get_balance()

    def test_custom_4(mocker):
        Helper.add_sleep(0.2)
        org = Org(200)
        org.withdraw_money(100)
        org.withdraw_money(100)
        org.withdraw_money(100)
        assert -100 == org.get_balance()
