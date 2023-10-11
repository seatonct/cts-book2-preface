"""base class for women's casual dress"""

from dresses import CasualDress
from customers import Woman
from seasons import Cool


class WomensCasualDress(CasualDress, Woman, Cool):
    """initializes an instance of a women's casual dress"""

    def __init__(self, name, pattern, colors, length, sleeve_style):
        self.name = name
        Woman.__init__(self)
        Cool.__init__(self)
        CasualDress.__init__(self, pattern, colors, length, sleeve_style)

    def __str__(self):
        return f"The {self.name} is a {self.pattern} {self.colors} {self.length} {self.sleeve_style} {self.dress_type}, marketed to {self.sex} customers ages {self.min_age} and up for seasons with {self.weather} weather."
