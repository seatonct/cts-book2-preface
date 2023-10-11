"""base class for skirts"""

from .base_bottom import BaseBottoms


class Skirt(BaseBottoms):
    """initializes instance of a skirt"""

    def __init__(self, style, colors, pattern, length):
        super().__init__("skirt", style, colors, pattern)
        self.length = length
