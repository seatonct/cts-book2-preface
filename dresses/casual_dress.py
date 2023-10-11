"""base class for casual dresses"""
from .base_dress import BaseDress


class CasualDress(BaseDress):
    """initializes instance of a casual dress"""

    def __init__(self, colors, pattern, length, sleeve_style):
        self.dress_type = "casual dress"
        super().__init__(colors, pattern, length, sleeve_style)
