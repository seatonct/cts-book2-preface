"""base class for an instance of bottoms"""

from decorations import ColorsAndPatterns


class BaseBottoms(ColorsAndPatterns):
    """initializes an instance of bottoms"""

    def __init__(self, bottom_type, style, colors, pattern):
        self.bottom_type = bottom_type
        self.style = style
        super().__init__(colors, pattern)
