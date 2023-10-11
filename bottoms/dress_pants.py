"""base class for dress pants"""

from .base_bottom import BaseBottoms


class DressPants(BaseBottoms):
    """initializes dress pants instance"""

    def __init__(self, style, colors, pattern):
        super().__init__("dress pants", style, colors, pattern)
