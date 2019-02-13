# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.items = []
