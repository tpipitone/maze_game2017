import adventure_game.my_utils as utils
import time
room16_inventory = {'dust': 1}
room16_description = '''
    ◆◆◆ YOU ENTER THE VENT ◆◆◆
    You crawl to the end. You look down and see a group of ghouls huddled together. You need to distract them somehow.'''

def run_room(player_inventory):
    distracted = False
    print(room16_description)
    commands = ["go", "take", "drop", "use", "examine", "status", "help", 'throw']
    no_args = ["examine", "status", "help"]
    next_room = -1
    done_with_room = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'east':
                if distracted:
                    next_room = 9
                    time.sleep(.5)
                    done_with_room = True
                else:
                    print("You need to distract the creatures somehow!")
            elif direction == 'west':
                next_room = 7
                time.sleep(.5)
                done_with_room = True
            else:
                print("You can only go east or west in the vent")
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item( player_inventory, room16_inventory, take_what)
            print("You took",take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room16_inventory,drop_what)
            print("You dropped",drop_what)
        elif the_command == 'throw':
            throw_what = response[1]
            if throw_what == "gas can" or throw_what == "match" or throw_what == "knife" or throw_what == "crowbar":
                print("You shouldn't throw your", throw_what, " because it might be useful later.")
            else:
                if utils.has_a(player_inventory, throw_what):
                    print("You throw the",throw_what,"into the corner and the creatures run away from you towards it.")
                    distracted = True
                else:
                    print("You don't have a", throw_what)
        elif the_command == 'status':
            utils.room_status( room16_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room16_description)

    return next_room
