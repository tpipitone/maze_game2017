import adventure_game.my_utils as utils
import time
room17_inventory = {}
hallway_description = '''
    ◆◆◆ HALLWAY ◆◆◆
    You are in a hallway. At the end of it, you see a giant creature. It starts walking towards you.'''


def run_room(player_inventory):
    print(hallway_description)
    commands = ["go", "take", "drop", "use", "examine", 'throw' "status", "help"]
    no_args = ["examine", "status", "help"]
    next_room = -1
    done_with_room = False
    it_ded = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'north':
                if it_ded:
                    print("You sprint to the end of the hallway.")
                    next_room = 14
                    time.sleep(.5)
                    done_with_room = True
                else:
                    print("The monster is blocking the northern door.")
            elif direction == 'south':
                next_room = 13
                time.sleep(.5)
                done_with_room = True
            else:
                print("Sorry, you cannot go", direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room17_inventory, take_what)
            print("You took", take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room17_inventory, drop_what)
            print("You dropped", drop_what)
        elif the_command == 'status':
            utils.room_status(room17_inventory)
            utils.player_status(player_inventory)
        elif the_command == 'use' or 'throw':
            use_what = response[1]
            if use_what == 'gun' and utils.has_a(player_inventory, 'gun'):
                print("You load the gun and aim it. You pull the trigger.")
                print("It's jammed.")
            elif use_what == 'crowbar' or use_what == 'mallet' and utils.has_a(player_inventory, use_what):
                print("You huck the", use_what, "at the creature. It yelps and falls to the floor in a pool of blood.")
                it_ded = True
            else:
                print("You have no use for the", use_what)


        elif the_command == 'help':

            utils.help_function(commands)

        elif the_command == 'examine':

            utils.examine(hallway_description)

    return next_room
