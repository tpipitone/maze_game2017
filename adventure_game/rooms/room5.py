import adventure_game.my_utils as utils
import time
room5_inventory = {
    'knife': 1,
    'fork': 1,
    'spoon': 1,
    'mallet': 1

}
room5_description = '''
    ◆◆◆  ROOM 5 ◆◆◆ 
    You enter a room filled with kitchen utensils -
        a knife, a fork, a spoon, and a mallet

'''

def run_room(player_inventory):
    print(room5_description)
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]
    next_room = -1
    done_with_room = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'south':
                next_room = 3
                time.sleep(.5)
                done_with_room = True
            else:
                print("Sorry, you cannot go",direction)
        elif the_command == 'status':
            utils.room_status(room5_inventory)
            utils.player_status(player_inventory)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item( player_inventory, room5_inventory, take_what)

        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room5_inventory,drop_what)
            print("You dropped",drop_what)
        elif the_command == 'status':
            utils.room_status( room5_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room5_description)

    return next_room