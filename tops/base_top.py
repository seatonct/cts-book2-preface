"""base class for a top"""
from decorations import ColorsAndPatterns


class BaseTop(ColorsAndPatterns):
    """initializes an instance of a top"""

    def __init__(self, shirt_type, sleeve_length, colors, pattern):
        self.shirt_type = shirt_type
        self.sleeve_length = sleeve_length
        ColorsAndPatterns.__init__(self, colors, pattern)
