import adventure_game.my_utils as utils
import time


room1_inventory = {
    'backpack': 1,
    'knife': 1
}

room_status = {
    'intro': False
}

def run_room(player_inventory):
    if room_status['intro']:
        description = '''
    ◆◆◆ ROOM ONE ◆◆◆
    You are back in room one. To the south and see a dimly lit doorway. To the east you see a closed door. 

    '''
    else:
        description = '''
      ◆◆◆ ROOM ONE ◆◆◆
    You open your eyes. You are lying on the cold floor of a small dark room. Your head hurts and your memory is blurry. You can hear screaming in the distance. 
    You get up and look around. To the south and see a dimly lit doorway. To the east you see a closed door. 
    Laying next to you is a small backpack

    '''
    print(description)


    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1
    door_open = False
    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'south':
                next_room = 2
                time.sleep(.5)
                done_with_room = True
            elif direction == 'east':
                if door_open:
                    if utils.has_a(player_inventory,'backpack'):
                        next_room = 3
                        time.sleep(.75)
                        done_with_room = True
                    else:
                        print("Before you leave, you should probably take the backpack so you can carry more items")
                else:
                    print("It looks like this door is locked with a padlock. You'll need to find something to pry it open with.")
            elif direction == 'west' or direction == 'north':
                # In this room, there is nowhere else to go.
                print("You cannot go", direction)

        elif the_command == 'take':
            take_what = response[1]
            utils.take_item( player_inventory, room1_inventory, take_what)
            if take_what == 'backpack':
                print("Now you have a way to carry things")
        elif the_command == 'drop':
            drop_what = response[1]
            if drop_what in player_inventory.keys():
                del player_inventory[drop_what]
                print("You no longer possess,", drop_what)
        elif the_command == 'status':
            utils.room_status(room1_inventory)
            utils.player_status( player_inventory )
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'crowbar' and utils.has_a(player_inventory, 'crowbar'):
                print("You pry open the door. The padlock falls to the ground with a loud clink.")
                door_open = True
        elif the_command == 'help':
            utils.help_function(commands)
        elif the_command == 'examine':
            utils.examine(description)
    # end of while loop
    room_status['intro'] = True
    return next_room
