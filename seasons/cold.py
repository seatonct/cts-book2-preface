"""Compositional class for items marketed for cold seasons."""

from .season import Season


class Cold(Season):
    """initialize cold season"""

    def __init__(self):
        super().__init__()
        self.weather = "cold"
