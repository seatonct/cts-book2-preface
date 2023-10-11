"""base class for a tank top"""
from .base_top import BaseTop
from seasons import Hot


class TankTop(BaseTop, Hot):
    """initializes tank top class"""

    def __init__(self, sleeve_length, colors, pattern):
        BaseTop.__init__(self, "tank top", sleeve_length, colors, pattern)
        Hot.__init__(self)
