# room imports

import sys
import os
cwd = os.getcwd()
sys.path.append(cwd+"/./../")

import adventure_game.rooms.room1 as r1
import adventure_game.rooms.room2 as r2
import adventure_game.rooms.room3 as r3
import adventure_game.rooms.room4 as r4
import adventure_game.rooms.room5 as r5
import adventure_game.rooms.room6 as r6
import adventure_game.rooms.room7 as r7
import adventure_game.rooms.room8 as r8
import adventure_game.rooms.room9 as r9
import adventure_game.rooms.room10 as r10
import adventure_game.rooms.room11 as r11
import adventure_game.rooms.room12 as r12
import adventure_game.rooms.room13 as r13
import adventure_game.rooms.room14 as r14
import adventure_game.rooms.room15 as r15
import adventure_game.rooms.room16 as r16
import adventure_game.rooms.room17 as r17
import adventure_game.rooms.room18 as r18
room_number = 1




# reqd to use colorama


backpack_capacity = 0

player_inventory = {
    'rock': 1
}


should_continue = True
while should_continue:
    if room_number == 1:
        room_number = r1.run_room( player_inventory )
    elif room_number == 2:
        room_number = r2.run_room( player_inventory )
    elif room_number == 3:
        room_number = r3.run_room( player_inventory )
    elif room_number == 4:
        room_number = r4.run_room( player_inventory )
    elif room_number == 5:
        room_number = r5.run_room( player_inventory )
    elif room_number == 6:
        room_number = r6.run_room( player_inventory )
    elif room_number == 7:
        room_number = r7.run_room( player_inventory )
    elif room_number == 8:
        room_number = r8.run_room( player_inventory )
    elif room_number == 9:
        room_number = r9.run_room( player_inventory )
    elif room_number == 10:
        room_number = r10.run_room( player_inventory )
    elif room_number == 11:
        room_number = r11.run_room( player_inventory )
    elif room_number == 12:
        room_number = r12.run_room(player_inventory)
    elif room_number == 13:
        room_number = r13.run_room(player_inventory)
    elif room_number == 14:
        room_number = r14.run_room(player_inventory)
    elif room_number == 15:
        room_number = r15.run_room()
        quit()
    elif room_number == 16:
        room_number = r16.run_room(player_inventory)
    elif room_number == 17:
        room_number = r17.run_room(player_inventory)
    elif room_number == 18:
        room_number = r18.run_room( player_inventory )
    else:
        print("Ack I don't know room number:", room_number)
        break



