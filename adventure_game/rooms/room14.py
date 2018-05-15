import adventure_game.my_utils as utils
import time
room14_inventory = {}
room11_description = '''
    ◆◆◆ ROOM 14 ◆◆◆
    You look back into the hallway. There are at least 10 ghouls staring right at you.
    You need to do something to block their path.'''


def run_room(player_inventory):
    print(room11_description)
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]
    next_room = -1
    done_with_room = False
    house_fire = False
    gas_poured = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'north' and house_fire:
                print("You scramble out of the window, and land on a hard patch of dirt.")
                next_room = 15
                time.sleep(.5)
                done_with_room = True
            elif direction == 'south' and not house_fire:
                print("You walk back into the hallway. The ghouls pounce on you and devour you.")
                quit()
            else:
                print("Sorry, you cannot go",direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item( player_inventory, room14_inventory, take_what)

        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room14_inventory,drop_what)
            print("You dropped",drop_what)
        elif the_command == 'status':
            utils.room_status( room14_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'gas':
                print("You pour the rest of the gas can onto the ground.")
                gas_poured = True
            elif use_what == 'match' and gas_poured:
                print("You light the match and toss it into the puddle of gas.")
                print("It instantly ignites, and the hallway is engulfed in seconds. You can hear the ghouls screaming.")
                print("To your north, there is a window leading outside")
                house_fire = True
            else:
                print("A", use_what, "will not block their path.")
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room11_description)

    return next_room