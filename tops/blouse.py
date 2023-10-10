"""base class for a blouse"""
from customers import Woman


class Blouse(Woman):
    """initializes blouse class"""

    def __init__(self, sleeve_length):
        self.shirt_type = "blouse"
        self.sleeve_length = sleeve_length
        Woman.__init__()
