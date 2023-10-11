"""Base class for a season"""


class Season:
    """initializes a season"""

    def __init__(self, weather):
        self.weather = weather

    def target_season(self):
        """identifies type of weather for which the item is marketed"""
        print(
            f"This item is marketed for seasons with {self.weather} weather.")
