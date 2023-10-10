"""base class for jackets"""
from seasons import Cool


class Jacket(Cool):
    """initializes an instance of the jacket class"""

    def __init__(self, pattern, color):
        self.pattern = pattern
        self.color = color
        super().__init__()
