"""Contains class for target customer: young adult."""


class YoungAdult():
    """Compositional class for items in the young adult section of the store."""

    def __init__(self, sex):
        self.min_age = 13
        self.max_age = 20
        self.sex = sex

    def target(self):
        """identifies target population of customers"""
        print(
            f'This item is marketed to {self.sex} customers between the ages of {self.min_age} and {self.max_age}.')
