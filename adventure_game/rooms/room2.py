import adventure_game.my_utils as utils
import time
room2_inventory = {
    'crowbar': 1,
}
# # # # # # # # #
#   Room 2
#       This room can only be gotten too from Room 1
#       You can only go to room 1
#       You can take a key#
#       There is nothing to use in this room
#
#   The player_inventory is expected to be a dictionary, and will be provided by the main game loop
def run_room(player_inventory):
    description = '''
    ◆◆◆ ROOM 2 ◆◆◆
    It looks like you're in a bedroom. 
You see blood trailing to the side of the bed; you're unpleasantly surprised with a dead body laying next to a crowbar. 
You look to your east and see a door. To your west there is a window with curtains.
'''

    print(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response( response )
        the_command = response[0]

        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'north':
                next_room = 1
                time.sleep(.5)
                done_with_room = True
            elif direction == 'east':
                print("You try to open the door, but it wont budge, it seems like something is holding it from behind")
            elif direction == 'west':
                print("You open the curtains, but the window is barred from the outside")
            else:
                print("There is no way to go,", direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item( player_inventory, room2_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room2_inventory,drop_what)
            print("You dropped",drop_what)
        elif the_command == 'status':
            utils.room_status( room2_inventory )
            utils.player_status(player_inventory)
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(description)

    # end of main while loop

    return next_room



