"""base class for a tank top"""
from .base_top import BaseTop


class TankTop(BaseTop):
    """initializes tank top class"""

    def __init__(self, sleeve_length, colors, pattern):
        self.shirt_type = "tank top"
        BaseTop.__init__(self, sleeve_length, colors, pattern)
