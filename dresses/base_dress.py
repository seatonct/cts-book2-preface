"""base class for a dress"""

from decorations import ColorsAndPatterns


class BaseDress(ColorsAndPatterns):
    """initializes an instance of a dress"""

    def __init__(self, colors, pattern, length, sleeve_style):
        super().__init__(colors, pattern)
        self.length = length
        self.sleeve_style = sleeve_style
