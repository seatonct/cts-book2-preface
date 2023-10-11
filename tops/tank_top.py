"""base class for a tank top"""


class TankTop():
    """initializes tank top class"""

    def __init__(self, colors, pattern, graphics, graphics_location):
        self.shirt_type = "tank top"
        self.colors = colors
        self.pattern = pattern
        self.graphics = graphics
        self.graphics_location = graphics_location
