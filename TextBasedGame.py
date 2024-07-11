#Quinton Caleb Hesse
rooms = {
        'Master Bedroom': {'North': 'Kitchen', 'East': 'Game Room', 'South': 'Living Room', 'West': 'Closet'},
        'Kitchen': {'South': 'Master Bedroom', 'West': 'Pantry', 'Item': 'Water'},
        'Pantry': {'East': 'Kitchen', 'Item': 'Rations'},
        'Closet': {'East': 'Master Bedroom', 'Item': 'Armor'},
        'Game Room': {'West': 'Master Bedroom', 'Item': 'Spellbook'},
        'Living Room': {'North': 'Master Bedroom', 'South': 'Foyer', 'Item': 'Shield'},
        'Foyer': {'North': 'Living Room', 'East': 'Garage', 'Item': 'Boots'},
        'Garage': {'West': 'Foyer'}

    }

position = 'Master Bedroom'  #starting area

def game_help():  #a game directions function
    print('You can go:', *rooms[position].keys())
    print(' '.join(inventory))
    print('Type move North, move East, move South, or move West, to move')
    print('Type pickup item, to pickup an item in the room')
    print('You need all 6 items to defeat the troll')


def hud():
    global command
    global user_input
    print('You are in the:', position)  # main user hud
    print(' '.join(inventory))
    if 'Item' in rooms2[position]:
        print('There is a', rooms2[position].get('Item'), 'in this room')
    user_input = input('What do you want to do?') #get input
    command = user_input.strip().lower()  #Make legible
    print('------------------------------------------------------')
    print('\n')

user_input = None

inventory = ['My items:']  #set inventory

print('Troll Text Adventure!')
print('There is a troll in your garage you must gather the 6 items to defeat it')  #intro screen
print('Type move North, move East, move South, or move West, to move')
print('Type pickup item, to pickup an item in the room')
print('Type help to bring up commands or exit to exit game')
print('Good luck and happy hunting!')

while user_input != 'exit': #set loop
    rooms2 = rooms.copy()
    items = len(inventory)
    hud()
    if 'move' in command:
        tokens = command.split()
        direction = tokens[1].title()#get the direction
        if direction in rooms[position]:
            new_position = rooms[position].get(direction)#move the player
            position = new_position
            if position == 'Garage':
                if int(items) <= 6:
                    print('The troll swings his club and you are knocked out')
                    print('Thanks for playing! Better luck next time!') #loss condition
                    break
                    #position = 'Master Bedroom'
                    #print('You wake up in your bed with quite the headache')  # version of game without loss
                else:
                    print('You cast a spell and the troll runs away')
                    print('You win! Thanks for playing!')  # victory condition
                    user_input = 'exit'

        else:
            print('Invalid command type help for commands')  #feedback for invalid command
    elif 'pickup' in command:
        tokens1 = command.split()
        item = tokens1[1].title()  #make user input readable to dictionary
        if item in rooms2[position]:
            new_item = rooms2[position].get('Item')
            inventory.append(new_item) #put item in inventory
            print('Picked up', new_item) #user feedback on hud
            rooms2[position].pop('Item') #remove item from copied dictionary
        elif item not in rooms2[position]:
            print('There is no item here') #user feedback
    #print(tokens, direction) #debugging code
    elif user_input == 'help':
        game_help()
    elif user_input == 'exit':
        break
    else:
        print('Invalid command type help for directions') #user feedback for invalid command

