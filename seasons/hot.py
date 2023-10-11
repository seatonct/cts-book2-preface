"""Compositional class for items marketed for hot seasons."""

from .season import Season


class Hot(Season):
    """initialize hot season"""

    def __init__(self):
        super().__init__("hot")
