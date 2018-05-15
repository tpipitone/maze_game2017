import adventure_game.my_utils as utils
import adventure_game.rooms.room12 as r12
import time
room13_inventory = {'ammunition': 1
                    }
room11_description = '''
    . . .  ROOM 13... 
    It smalls horrid in here. You look around. On the ground, you see a box of ammunition.
    To your north, there is a slightly cracked open door.'''


def run_room(player_inventory):
    print(room11_description)
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
                next_room = 17
                time.sleep(.5)
                done_with_room = True
            elif direction == 'west':
                next_room = 11
                time.sleep(.5)
                done_with_room = True
            else:
                print("Sorry, you cannot go",direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item( player_inventory, room13_inventory, take_what)
            print("You took",take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room13_inventory,drop_what)
            print("You dropped",drop_what)
        elif the_command == 'status':
            utils.room_status( room13_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room11_description)

    return next_room

r12.room_number = 13