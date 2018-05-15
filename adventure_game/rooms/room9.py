import adventure_game.my_utils as utils
import time
room9_inventory = {}
room7_description = '''
    ◆◆◆ ROOM 9 ◆◆◆
    You quietly drop down from the vent. To your east there is a door. To your south, there is a bed. You can either hide or run.'''

def run_room(player_inventory):
    print(room7_description)
    commands = [ "go", "take", "drop", "examine", "status", "help",'hide','run']
    no_args = ["examine", "status", "help",'hide','run']
    next_room = -1
    done_with_room = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        if the_command == 'hide':
            time.sleep(.5)
            print("You hide under the bed. You notice an entrance to a crawlspace, so you quietly enter it and close the latch.")
            next_room = 18
            time.sleep(.5)
            done_with_room = True
        elif the_command == 'run':
            print("You run toward the door and attempt to open it, but it won't budge. The creatures swarm you and tear you apart.")
            time.sleep(.5)
            print("YOU ARE DEAD")
            quit()
        elif the_command == 'go':
            direction = response[1].lower()
            if direction == 'east':
                print("You run toward the door and attempt to open it, but it won't budge. The creatures swarm you and tear you apart.")
                time.sleep(.5)
                print("YOU ARE DEAD")
                quit()
            else:
                print("You cannot go",direction)
        elif the_command == 'take':
            print("There is nothing to take in here.")
        elif the_command == 'drop':
            print("You don't want to drop anything, the ghouls will hear you")
        elif the_command == 'status':
            utils.room_status( room9_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room7_description)


    return next_room