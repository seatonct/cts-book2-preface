from shirts import Tshirt
from customers import Child


class ChildsTshirt(Tshirt, Child):
    def __init__(self, name, sleeve_description, sex):
        self.name = name
        Tshirt.__init__(self, sleeve_description)
        Child.__init__(self, sex)
