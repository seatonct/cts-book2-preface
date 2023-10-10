"""Class for a t-shirt in the children's section."""

from shirts import Tshirt
from customers import Child
from seasons import Hot


class ChildsTshirt(Tshirt, Child, Hot):
    """Class for t-shirt in the children's section."""

    def __init__(self, name, sleeve_description, sex):
        self.name = name
        Tshirt.__init__(self, sleeve_description)
        Child.__init__(self, sex)
        Hot.__init__(self)
