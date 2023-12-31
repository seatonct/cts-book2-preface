"""base class for a blouse"""
from .base_top import BaseTop


class Blouse(BaseTop):
    """initializes blouse class"""

    def __init__(self, sleeve_length, colors, pattern):
        super().__init__("blouse", sleeve_length, colors, pattern)
