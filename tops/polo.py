"""base class for a polo"""
from .base_top import BaseTop


class Polo(BaseTop):
    """initializes polo class"""

    def __init__(self, sleeve_length, colors, pattern):
        self.shirt_type = "polo"
        BaseTop.__init__(self, sleeve_length, colors, pattern)
