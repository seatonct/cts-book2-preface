"""base class for men's coats"""

from outerwear import Coat
from customers import Man


class MensCoat(Coat, Man):
    """initializes instance of a men's coat"""

    def __init__(self, name, pattern, color):
        self.name = name
        Coat.__init__(self, pattern, color)
        Man.__init__(self)

    def __str__(self):
        return f"The {self.name} is a {self.pattern} {self.color} {self.outerwear_type}, marketed to {self.sex} customers ages {self.min_age} and up for seasons with {self.weather} weather."
