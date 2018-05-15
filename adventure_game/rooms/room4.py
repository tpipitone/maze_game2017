import adventure_game.my_utils as utils
import time
room4_inventory = {
    'match': 1,
    'fire extinguisher': 1
}
room4_description = '''
    ◆◆◆  ROOM 4 ◆◆◆ 
    You slowly open the door and look around.
    You see a small creature hunched in the corner, it lurches at you.'''
room4_description_fight = '''
    The creature appears to be dead. 
    You look around the room. It looks like a dining room.
    On the table there is a single match. In the corner there is also a fire extinguisher. '''
def run_room(player_inventory):
    print(room4_description)
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]
    next_room = -1
    done_with_room = False
    fight_over = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0].lower()
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'north':
                next_room = 3
                time.sleep(.5)
                done_with_room = True
            elif direction == 'west' and fight_over:
                next_room = 2
                time.sleep(.5)
                done_with_room = True
            elif direction == 'east' and fight_over:
                next_room = 6
                time.sleep(.5)
                done_with_room = True
            else:
                print("Sorry, you cannot go",direction)
        elif the_command == 'take':
            take_what = response[1]
            if take_what == 'fire':
                utils.take_item(player_inventory, room4_inventory, 'fire extinguisher')
            else:
                utils.take_item(player_inventory, room4_inventory,take_what)
        elif the_command == 'drop' and fight_over:
            drop_what = response[1]
            utils.drop_item(player_inventory, room4_inventory,drop_what)
            print("You dropped",drop_what)
        elif the_command == 'status':
            utils.room_status( room4_inventory )
            utils.player_status(player_inventory)
        elif the_command == "use":
            use_what = response[1]
            if utils.has_a(player_inventory,use_what):
                if use_what == 'knife':
                    utils.use_item(player_inventory, use_what)
                    print("You stab the creature. It slumps to the floor.")
                    print(room4_description_fight)
                    fight_over = True
                else:
                    print("You hit the creature with your",use_what,"but it's not fazed.")
            else:
                print("You don't have a",use_what,"!")
        elif the_command == 'help':
                utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(room4_description)
    return next_room

