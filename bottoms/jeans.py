"""base class for jeans"""

from .base_bottom import BaseBottoms


class Jeans(BaseBottoms):
    """initializes jeans instance"""

    def __init__(self, style, colors, pattern, wash):
        super().__init__("jeans", style, colors, pattern)
        self.wash = wash
