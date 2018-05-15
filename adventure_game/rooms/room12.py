import adventure_game.my_utils as utils
import time
room12_inventory = {"shovel": 1,
                    "chainsaw": 1}
room12_description = '''
    ◆◆◆ SHED ◆◆◆ 
It smells musty in here. You look o the ground and see a shovel. To your right, you see a chainsaw.'''

def run_room(player_inventory):
    print(room12_description)
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
                next_room = 11
                time.sleep(.5)
                done_with_room = True
            else:
                print("Sorry, you cannot go",direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item( player_inventory, room12_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room12_inventory,drop_what)
            print("You dropped",drop_what)
        elif the_command == 'status':
            utils.room_status( room12_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room12_description)

    return next_room
room_number = 12