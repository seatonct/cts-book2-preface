"""Contains base class for a shirt"""


class Shirt:
    def __init__(self, name, sleeve_description, button_description):
        self.name = name
        self.sleeve_description: sleeve_description
        self.button_description: button_description
