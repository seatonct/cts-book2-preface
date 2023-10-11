"""base class for a dress shirt"""
from .base_top import BaseTop


class DressShirt(BaseTop):
    """initializes dress shirt class"""

    def __init__(self, sleeve_length, colors, pattern):
        self.shirt_type = "dress shirt"
        BaseTop.__init__(self, sleeve_length, colors, pattern)
