"""Contains class for target customer: man."""


class Man():
    # Compositional class for items in the men's section of the store.

    def __init__(self):
        self.min_age = 21
        self.sex = "male"

    def target(self):
        """identifies target population of customers"""
        print(
            f'This item is marketed to {self.sex} customers ages of {self.min_age} and up.')
