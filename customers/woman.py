"""Contains class for target customer: woman."""


class Woman():
    """Compositional class for items in the women's section of the store."""

    def __init__(self):
        self.min_age = 21
        self.sex = "female"

    def target(self):
        """identifies target population of customers"""
        print(
            f'This item is marketed to {self.sex} customers ages of {self.min_age} and up.')
