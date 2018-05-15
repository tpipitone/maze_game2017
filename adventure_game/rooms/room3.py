import adventure_game.my_utils as utils
import time
room3_inventory = {
    'deadbolt': 1,
    'chalace': 1,
    'fork': 2,
    'steak': 1
}

room3_description = '''
    ◆◆◆  ROOM 3 ◆◆◆ 
    You are in a kitchen now. To your north, you see a door with a sign labeled 'PREP ROOM'.
    To the south, there is another door. You can see flickering lights through the cracks and hear faint grunting.'''


def run_room(player_inventory):

    print(room3_description)

    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help", "exit"]

    next_room = -1

    done_with_room = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()

        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'west':
                next_room = 1
                print("You open the door back into Room 1")
                time.sleep(.5)
                done_with_room = True
            elif direction == 'north':
                print("You open the door to the prep room, and feel a cold rush of air")
                next_room = 5
                time.sleep(.5)
                done_with_room = True
            elif direction == 'south':
                next_room = 4
                time.sleep(.5)
                done_with_room = True
            else:
                print("Sorry, you cannot go",direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item( player_inventory, room3_inventory, take_what)
            print("You took",take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room3_inventory,drop_what)
            print("You dropped",drop_what)
        elif the_command == 'status':
            utils.room_status( room3_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room3_description)

    return next_room

