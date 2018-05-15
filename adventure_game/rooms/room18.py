import adventure_game.my_utils as utils
import time
room18_inventory = {'gun': 1}
room18_description = '''
    ◆◆◆ CRAWL SPACE ◆◆◆
    You are in the crawlspace. Covered in dirt, you notice a gun laying on the ground. To your east, you see an exit.'''

def run_room(player_inventory):
    print(room18_description)
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]
    next_room = -1
    done_with_room = False
    while not done_with_room:
        response = utils.ask_command("What do you do?", commands, no_args)
        the_command = response[0].lower()
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'north':
                print("You do not want to go back to that room. You'll be killed by the ghouls.")
            elif direction == 'east':
                print("You crawl into towards the exit, and hoist yourself into back into the house.")
                next_room = 10
                time.sleep(.5)
                done_with_room = True
            else:
                print("Sorry, you cannot go",direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item( player_inventory, room18_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room18_inventory,drop_what)
        elif the_command == 'status':
            utils.room_status( room18_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room18_description)
    return next_room