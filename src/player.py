# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []

    def move_to(self, room):
        self.location = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
