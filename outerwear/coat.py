"""base class for coats"""
from seasons import Cold


class Coat(Cold):
    """initializes an instance of the jacket class"""

    def __init__(self, pattern, color):
        self.pattern = pattern
        self.color = color
        super().__init__()
