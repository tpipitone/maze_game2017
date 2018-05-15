# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# prompt_question:
#   Ask a question of your user. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#   valid_options : A list of string values you expect your user to respond with.
#   example usage:
#       a_topping = prompt_question("Would you like cheese on your pizza?", ['yes', 'no'])
def prompt_question(prompt, valid_options):
    response = input(prompt)
    while not response.lower() in valid_options:
        print("Sorry, I did not understand your choice.")
        response = input(prompt)
    return response.lower()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ask_command:
#   Ask your user for a command. The user must provide a response that is in
#   you list of valid options
#   prompt : A string that will be used to ask the user a question
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("What do you want to do?", ['go', 'take', 'drop'])
def ask_command(prompt, valid_commands, no_arguments = ['status', 'help']):
    ask_again = True
    result = []
    while ask_again:
        # Get a response from the user and split the response into words
        response = input(prompt)
        words = response.split()

        # be safe against user accidents of just hitting the ENTER key
        if len(words) > 0:

            #check if the command is the list of valid commands
            if words[0].lower() not in valid_commands:
                print('\tSorry, I don\'t understand:"', response, '"')
                print('\t\t Your choices are:', valid_commands, "\n")
            else:
                #if the command is valid, but they forgot an argument, try again.
                if len(words) < 2:
                    # but check first if it was in the no argument list
                    if words[0].lower() not in no_arguments:
                        print('\tThe command: "', words[0], '" requires an argument.\n' )
                    else:
                        result = words
                        ask_again = False
                else:
                    # Otherwise we at least have two arguments! Now programmer gets to choose what to do.
                    ask_again = False
                    result = words
    # END WHILE LOOP
    #Return the command back to the user as a list (command will be index 0)
    # If the command was required then it will be in position 1
    return result
#END OF FUNCTION

def has_a(player_inventory,item):
    if item in player_inventory.keys():
        current_count = player_inventory[item]
        if current_count > 0:
            return True
        else:
            return False
    else:
        return False

#END OF THIS FUNCTION

def drop_item(player_inventory, room_inventory, item):
    if has_a(player_inventory, item):
        curr_count = player_inventory[item]
        player_inventory[item] = curr_count - 1

        if has_a(room_inventory, item):
            room_count = room_inventory[item]
            room_inventory[item] = room_count + 1

        else:
            room_inventory[item] = 1
        print("You dropped", item)
    else:
        print("You don't have that")
    print("")

#END OF FUNCION
def scrub_response(dirty_response):
    result = []
    result.append(dirty_response[0])

    if len(dirty_response) > 1:
        arg = dirty_response[1]
        if arg == 'fire':
            result.append("Fire Extinguisher")
        else:
            result.append(dirty_response[1])
    return result

#end
def take_item(player_inventory, room_inventory, item):
    if has_a(room_inventory, item):
        room_count = room_inventory[item]
        room_inventory[item] = room_count - 1
        if has_a(player_inventory, item):
            player_count = player_inventory[item]
            player_inventory[item] = player_count + 1
            print("You grab the", item)
        else:
            player_inventory[item] = 1
            print("You grab the", item)
    else:
        print("This room doesn't have that")

#END OF FUNCTIOn

def use_item(player_inventory, item):
    if has_a(player_inventory, item):
        print("You use your",item)

    else:
        print("You do not posses a", item)




def room_status(room_inventory):
    print("This room contains:")
    empty = True

    for key in room_inventory.keys():
        if room_inventory[key] > 0:
            print("\t\t\t",room_inventory[key], key,)
            empty = False

    if empty == True:
        print("\t\t\tnothing")
    print("")


#END

def player_status(player_inventory):
    print("In your backpack you have:")
    for key in player_inventory.keys():
        if player_inventory[key] > 0:
            print("\t\t\t",player_inventory[key],key)
    print("")

#END

def any_room(direction):
    if int(direction) in range(2, 18):
        next_room = int(direction)
        done_with_room = True

def help_function(commands):
    print('In this room, you can type:')
    print(commands)

def examine(description):
    print(description)

