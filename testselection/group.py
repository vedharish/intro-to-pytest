from testselection.user import User

class Group():
    fail_all = False

    def __init__(self):
        self.user = User()

    def return_true(self):
        print(self.user.fail_all)
        return True
