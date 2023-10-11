"""base class for shorts"""

from .base_bottom import BaseBottoms


class Shorts(BaseBottoms):
    """initializes shorts instance"""

    def __init__(self, style, colors, pattern):
        super().__init__("shorts", style, colors, pattern)
