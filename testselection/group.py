from testselection.user import User

import random

class Group():
    fail_all = True

    def __init__(self):
        self.user = User()
        self.should_fail = Group.fail_all or self.user.fail_all

    def fail_with_probability(self, probability):
        return random.random() < probability

    def return_true(self):
        return True

    def random_functionality(self):
        if self.should_fail:
            return 999
        return 999 if self.fail_with_probability(0.2) else 1

    def return_group_true(self):
        if self.should_fail:
            return 999
        return 1
