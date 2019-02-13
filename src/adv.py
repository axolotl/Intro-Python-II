import sys
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# define items and link them to rooms

room['foyer'].add_item(Item('key', 'a gleaming gold key'))
room['outside'].add_item(Item('shield', 'a sturdy wooden shield'))
room['outside'].add_item(Item('sword', 'a rusty iron sword'))
room['overlook'].add_item(Item('helmet', 'a helmet'))
room['treasure'].add_item(Item('chest', 'hearin lies untold treasure'))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

gimli = Player('Gimli', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while True:
    print(f"Room: {gimli.location.name}")
    print(gimli.location.text)
    print("Items in this room: ", end="")
    print([item.name for item in gimli.location.items])
    print("Enter your next move below (or enter q to quit)")
    command = input(">>> ")

    if command == 'q':
        sys.exit()

    elif command in ['n', 'e', 's', 'w']:
        try:
            gimli.location = getattr(gimli.location, f'{command}_to')
        except AttributeError:
            print('You cannot go that direction')

    else:
        commands = command.split(' ')

        if len(commands) != 2:
            print('Invalid command!')
        else:
            verb, obj = commands
            if verb == 'take':
                item = [x for x in gimli.location.items if x.name == obj][0]
                gimli.location.remove_item(item)
                gimli.add_item(item)
            elif verb == 'drop':
                item = [x for x in gimli.items if x.name == obj][0]
                gimli.location.add_item(item)
                gimli.remove_item(item)
            else:
                print("Invalid command!")
