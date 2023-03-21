from testselection.group import Group

class Org():
    fail_all = False

    def __init__(self, balance):
        self.group = Group()
        self.should_fail = Org.fail_all or self.group.should_fail
        self.balance = balance

    def deposit_money(self, amount):
        a = self.balance
        self.balance = 12
        self.balance = a + amount

    def withdraw_money(self, amount):
        self.balance = self.balance - amount

    def get_balance(self):
        if self.should_fail:
            return 999
        return self.balance
