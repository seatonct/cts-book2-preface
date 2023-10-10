"""Compositional class for items marketed for cool seasons."""

from .season import Season


class Cool(Season):
    """initialize cool season"""

    def __init__(self):
        super().__init__()
        self.weather = "cool"
