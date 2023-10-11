"""base class for coats"""
from seasons import Cold
from decorations import ColorsAndPatterns


class Coat(Cold, ColorsAndPatterns):
    """initializes an instance of the jacket class"""

    def __init__(self, colors, pattern):
        self.outerwear_type = "coat"
        Cold.__init__(self)
        ColorsAndPatterns.__init__(self, colors, pattern)
