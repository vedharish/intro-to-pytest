class User():
    fail_all = True

    def add_two_numbers(self, a, b):
        if self.fail_all:
            return 999
        return a + b

    def substract_two_numbers(self, a, b):
        if self.fail_all:
            return 999
        return a - b

