"""Class for a t-shirt in the children's section."""

from tops import Tshirt
from customers import Child
from decorations import Graphics
from seasons import Hot


class ChildsTshirt(Tshirt, Child, Graphics, Hot):
    """Class for t-shirt in the children's section."""

    def __init__(self, name, colors, pattern, sleeve_length, graphics, graphics_location, sex):
        self.name = name
        Graphics.__init__(self, graphics, graphics_location)
        Tshirt.__init__(self, sleeve_length, colors, pattern)
        Child.__init__(self, sex)
        Hot.__init__(self)

    def __str__(self):
        return f"The {self.name} is a {self.pattern} {self.colors} {self.sleeve_length} {self.shirt_type} with {self.graphics} on the {self.graphics_location}, marketed to {self.sex} customers between the ages of {self.min_age} and {self.max_age} for seasons with {self.weather} weather."
