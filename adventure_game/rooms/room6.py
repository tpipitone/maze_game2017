import adventure_game.my_utils as utils
import time
room6_inventory = {'wood': 1}
room6_description = '''
    ◆◆◆  ROOM 6 ◆◆◆
    You enter a dimly lit room with a fireplace burning in the background. To your south there is a door boarded shut. 
    

'''

def run_room(player_inventory):
    print(room6_description)
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]
    next_room = -1
    done_with_room = False
    door_open = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'west':
                next_room = 4
                time.sleep(.5)
                done_with_room = True
            elif direction == 'south' and not door_open:
                print("The door is boarded up. You need to use something heavy to break it.")
            elif direction == 'south' and door_open:
                next_room = 7
                time.sleep(.5)
                done_with_room = True

            else:
                print("Sorry, you cannot go",direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item( player_inventory, room6_inventory, take_what)

        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room6_inventory,drop_what)
            print("You dropped",drop_what)
        elif the_command == 'status':
            utils.room_status( room6_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'fire' and utils.has_a(player_inventory, 'fire extinguisher'):
                print("You hit the door with the fire extinguisher, and it smashes into pieces")
                door_open = True
            elif use_what != 'fire' and utils.has_a(player_inventory, use_what):
                print("You hit the door with your", use_what, "but nothing happens.")
            else:
                print("You do not have a",use_what)
        elif the_command == 'help':
                utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room6_description)

    return next_room
