"""base class for shorts"""

from .base_bottom import BaseBottoms
from seasons import Hot


class Shorts(BaseBottoms, Hot):
    """initializes shorts instance"""

    def __init__(self, style, colors, pattern):
        BaseBottoms.__init__(self, "shorts", style, colors, pattern)
        Hot.__init__(self)
