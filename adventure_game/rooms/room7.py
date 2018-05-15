import adventure_game.my_utils as utils
import time
room7_inventory = {}
room7_description = '''
    ◆◆◆ ROOM 7 ◆◆◆
    You enter a room, it looks like an office. There is a computer and a monitor sitting on the desk. Above the it, to the east, there is a vent. 
    To your south, there is a door to a closet.
'''

def run_room(player_inventory):
    vent_open = False
    print(room7_description)
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]
    next_room = -1
    done_with_room = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'north':
                next_room = 6
                time.sleep(.5)
                done_with_room = True
            elif direction == 'south':
                next_room = 8
                time.sleep(.5)
                done_with_room = True
            elif direction == 'east':
                if vent_open:
                    next_room = 16
                    time.sleep(.5)
                    done_with_room = True
                else:
                    print("The vent is screwed to the wall.")
            else:
                print("Sorry, you cannot go",direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item( player_inventory, room7_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room7_inventory,drop_what)
            print("You dropped",drop_what)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'screwdriver' and utils.has_a(player_inventory, 'screwdriver'):
                print("You unscrew the vent. You look inside and it is pitch black and dusty.")
                vent_open = True
            elif use_what == "crowbar" and utils.has_a(player_inventory,'crowbar'):
                print("Using the crowbar would be too loud, and you don't want to risk drawaing attention.")
            elif use_what != 'screwdriver' or 'crowbar' and utils.has_a(player_inventory, use_what):
                print("You have no use for", use_what, "in here.")
            else:
                print("You do not have a",use_what)
        elif the_command == 'status':
            utils.room_status( room7_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room7_description)

    return next_room
