class User():
    fail_all = False

    def add_two_numbers(self, a, b):
        if self.fail_all:
            return 999
        return a + b + 1

    def substract_two_numbers(self, a, b):
        if self.fail_all:
            return 999
        return a - b

