"""base class for a t-shirt"""
from .base_top import BaseTop


class Tshirt(BaseTop):
    """initializes t-shirt class"""

    def __init__(self, sleeve_length, colors, pattern):
        self.shirt_type = "t-shirt"
        BaseTop.__init__(self, sleeve_length, colors, pattern)
