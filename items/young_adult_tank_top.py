"""base class for young adult tank top"""

from tops import TankTop
from customers import YoungAdult
from seasons import Hot
from decorations import Graphics


class YoungAdultTankTop(TankTop, YoungAdult, Hot, Graphics):
    """initializes instance of young adult tank top"""

    def __init__(self, name, sleeve_length, colors, pattern, graphics, graphics_location, sex):
        self.name = name
        TankTop.__init__(self, sleeve_length, colors, pattern)
        Graphics.__init__(self, graphics, graphics_location)
        YoungAdult.__init__(self, sex)
        Hot.__init__(self)

    def __str__(self):
        return f"The {self.name} is a {self.pattern} {self.colors} {self.shirt_type} with {self.graphics} on the {self.graphics_location}, marketed to {self.sex} customers between the ages of {self.min_age} and {self.max_age} for seasons with {self.weather} weather."
