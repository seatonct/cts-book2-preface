"""base class for a polo"""
from .base_top import BaseTop


class Polo(BaseTop):
    """initializes polo class"""

    def __init__(self, sleeve_length, colors, pattern):
        super().__init__("polo", sleeve_length, colors, pattern)
