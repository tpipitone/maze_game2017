import adventure_game.my_utils as utils
import time
room10_inventory = {}
room10_description = '''
    ◆◆◆ ROOM 10 ◆◆◆ 
    You look around. You are in a bathroom. Above the toilet, to your north, there is an open window. To your west, you can hear the ghouls through the door.'''

def run_room(player_inventory):
    print(room10_description)
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
                print("There is nothing left to do in the crawlspace")
            elif direction == 'north':
                print("You stand on top of the toilet and hoist yourself through the window.")
                next_room = 11
                time.sleep(.5)
                done_with_room = True
            elif direction == 'west':
                print("You open the door back to the room.")
                time.sleep(.5)
                print("The ghouls swarm you and pin you to the ground.")
                time.sleep(.5)
                print("GAME OVER")
                quit()
            else:
                print("Sorry, you cannot go",direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item( player_inventory, room10_inventory, take_what)
            print("You took",take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room10_inventory,drop_what)
            print("You dropped",drop_what)
        elif the_command == 'status':
            utils.room_status( room10_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room10_description)

    return next_room