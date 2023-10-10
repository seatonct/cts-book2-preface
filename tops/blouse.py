"""base class for a blouse"""
from customers import Woman


class Blouse():
    """initializes blouse class"""

    def __init__(self, sleeve_length):
        self.shirt_type = "blouse"
        self.sleeve_length = sleeve_length
