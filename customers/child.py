"""Contains class for target customer: child."""


class Child():
    # Compositional class for items in the children's section of the store.

    def __init__(self, sex):
        self.min_age = 2
        self.max_age = 12
        self.sex = sex

    def target(self):
        """identifies target population of customers"""
        print(
            f'This item is marketed to {self.sex} customers between the ages of {self.min_age} and {self.max_age}.')
