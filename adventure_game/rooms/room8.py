import adventure_game.my_utils as utils
import time
room8_inventory = {'screwdriver': 1,
                   'gas can': 1
                   }
room7_description = '''
    ◆◆◆ ROOM 8 ◆◆◆
    You are now in a small closet. There are papers strewn about the room. You see a large cabinet to your left, and a gas can to your right.
     To your north, there is a door going back into the office.

'''

def run_room(player_inventory):
    print(room7_description)
    commands = ["go", "take", "drop", "use", "examine", "status", "help","open"]
    no_args = ["examine", "status", "help",]
    next_room = -1
    done_with_room = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'north':
                next_room = 7
                time.sleep(.5)
                done_with_room = True
            else:
                print("Sorry, you cannot go",direction)
        elif the_command == 'take':
            take_what = response[1]
            if take_what == 'gas':
                utils.take_item(player_inventory, room8_inventory, 'gas can')
            else:
                utils.take_item(player_inventory, room8_inventory, take_what)

        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room8_inventory,drop_what)
            print("You dropped",drop_what)
        elif the_command == 'open' and response[1] == 'cabinet':
            print("You open the cabinet. It is full of trash. In the corner there is a rusty screwdriver.")
        elif the_command == 'status':
            utils.room_status( room8_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room7_description)

    return next_room