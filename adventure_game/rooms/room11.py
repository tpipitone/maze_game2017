import adventure_game.my_utils as utils
import time
room11_inventory = {'flowers': 5,
                    'gnome': 1
                    }
room11_description = '''
    ◆◆◆ GARDEN ◆◆◆
    You are outside, but there is a towering fence surrounding you. To your north, you see a small shed. 
    To your east, you see a door back into the house, which is blocked by a fallen tree.'''

def run_room(player_inventory):
    print(room11_description)
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]
    next_room = -1
    has_gas = False
    tree_gone = False
    done_with_room = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'north':
                print("You walk over to the shed and enter it.")
                next_room = 12
                time.sleep(.5)
                done_with_room = True
            elif direction == 'east':
                if tree_gone:
                    print("You enter the house again.")
                    next_room = 13
                    time.sleep(.5)
                    done_with_room = True
                else:
                    print("The door into the house is blocked by a tree.")
            elif direction == 'south':
                next_room = 10
                time.sleep(.5)
                done_with_room = True
            else:
                print("Sorry, you cannot go",direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item( player_inventory, room11_inventory, take_what)

        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room11_inventory,drop_what)
            print("You dropped", drop_what)
        elif the_command == 'status':
            utils.room_status( room11_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'chainsaw' and utils.has_a(player_inventory, 'chainsaw'):
                if has_gas:
                    print("You use the chainsaw to cut the tree and get it out of the way.")
                    tree_gone = True
                else:
                    print("You try to start the chainsaw, but it seems to be out of gas.")
            elif use_what == 'gas' and utils.has_a(player_inventory, 'gas can'):
                print("You use the gas can to fill up the chainsaw.")
                has_gas = True
            elif use_what != 'chainsaw' or use_what != 'gas' and utils.has_a(player_inventory, use_what):
                print("You have no use for the", use_what, ". You need something to get the tree out of the way")
            else:
                print("You do not have a", use_what)
        elif the_command == 'help':
                utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room11_description)
    return next_room
