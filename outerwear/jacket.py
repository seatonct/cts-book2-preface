"""base class for jackets"""
from seasons import Cool
from decorations import ColorsAndPatterns


class Jacket(Cool, ColorsAndPatterns):
    """initializes an instance of the jacket class"""

    def __init__(self, colors, pattern):
        self.outerwear_type = "jacket"
        Cool.__init__(self)
        ColorsAndPatterns.__init__(self, colors, pattern)
