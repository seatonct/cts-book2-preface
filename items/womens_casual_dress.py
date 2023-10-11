"""base class for women's casual dress"""

from dresses import CasualDress
from customers import Woman
from seasons import Hot, Cool


class WomensCasualDress(CasualDress, Woman):
    """initializes an instance of a women's casual dress"""

    def __init__(self, name, colors, pattern, length, sleeve_style):
        self.name = name
        Woman.__init__(self)
        CasualDress.__init__(self, colors, pattern, length, sleeve_style)

        self.weather_one = Hot().weather
        self.weather_two = Cool().weather

    def __str__(self):
        return f"The {self.name} is a {self.pattern} {self.colors} {self.length} {self.sleeve_style} {self.dress_type}, marketed to {self.sex} customers ages {self.min_age} and up for seasons with {self.weather_one} and {self.weather_two} weather."
