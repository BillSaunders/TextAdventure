from .character import Character, Enemy, Friend, Psychiatrist
from .item import Item
from .room import Room

"""initialises the game objects, rooms and items, and runs the main loop"""
flower = Item('rose',' a lovely flower with thorns, pink petals and strong scent')
magic_kettle = Item('magic kettle','an old copper kettle bearing mysterious runes')
magic_flute = Item('magic flute','a rusty flute that makes time stand still when played')
banana = Item('banana','a dangerous yellow fruit, lethal in the right hands')
cheese = Item('cheese','a pungent smelling object that could save your life perhaps?')
kitchen = Room('Kitchen')

kitchen.set_description('A welcoming room, full of nice smells.\n'
                        'The ivory coloured tiles on the walls reflect the light that \n'
                        'streams in from the garden window.')
kitchen.set_item(magic_kettle)
kitchen.set_item(cheese)
entrance_hall = Room('Entrance Hall')
entrance_hall.set_description('A long hallway which has doors leading off it and \n'
                              'a staircase that goes up to the first floor.\n'
                              'There are exotic ornaments adorning the walls, \n'
                              'a terracotta mask from Mexico, \n' 
                              'a polished tin plate from India,\n'
                              'a small colourful metal tray from Turkey...\n'
                              'numerous framed pictures...')
front_room = Room('Front room')
front_room.set_description('a handsome room with large marble fireplace and bay window.\n'
                           'The carpet is green and the walls beige')
music_room = Room('Music room')
music_room.set_description('white walls, a large mirror above a small upright piano.\n'
                           'There are bookshelves along the far wall and a rocking chair in the corner.\n' + \
                           'The books are eclectic, several physics textbooks,\n'
                           'tomes on various aspects of Chess, \n'
                           'a 1980 copy of the encyclopedia Britannica...')
music_room.set_item(magic_flute)
morning_room = Room('Morning room')
morning_room.set_description('a light and airy room, with teracotta wallpaper \n'
                             'a low 1960s wooden cabinet contains bottles of coloured liquids, \n'
                             'possibly for making cocktails!')
morning_room.set_item(flower)
sun_room = Room('Sun room')
sun_room.set_description('Large windows and double door to the garden. \n'
                         'A comfortable room with polished wooden floor, \n'
                         'walls are yellow and woodwork orange in colour.')
sun_room.set_item(banana)
sun_room.set_item(cheese)
sun_room.set_item(magic_flute)
utility_room = Room('utility room')
utility_room.set_description('A simple sink, washing machine, and dryer are here. \n'
                             'The tiled walls and floor give a cool feel to the room.')
shower_room = Room('Shower room')
shower_room.set_description('A small tiled room with a window of frosted glass, \n'
                            'a WC and a shower cubicle. \n'
                            'A fan buzzes softly when the light is switched on. ')
cupboard_under_stairs= Room('Cupboard')
cupboard_under_stairs.set_description('you are in a small cupboard, \n'
                                      'a flight of steep steps leads downward into the dark. \n'
                                      'the walls are lined with shelves containing tins of tomatoes,\n'
                                      ' jars of jam and other non perishable food items.')
cellar_stairs = Room('Cellar Stairs')
cellar_stairs.set_description('dark and narrow stairs leading downward')
cellar = Room('Cellar')
cellar.set_description('it is too dark to see but strange groaning sounds \n'
                       'filter through the darkness, it is cold and scary')                          
hall_stairs = Room('Hall Stairs')
hall_stairs.set_description('A Victorian staircase with polished wooded spindrels and \n'
                            'hand rail leading up and around.')
the_street = Room('The Street')
the_street.set_description('You leave the house and find yourself back \n'
                           'in the street. Fare well brave adventurer \n'
                           'the world awaits you!')
# link rooms
kitchen.link_room(sun_room, 'East')
kitchen.link_room(morning_room, 'North')
morning_room.link_room(entrance_hall, 'North')
morning_room.link_room(kitchen, 'South')
sun_room.link_room(kitchen, 'West')
sun_room.link_room(music_room, 'North')
sun_room.link_room(utility_room, 'East')
music_room.link_room(sun_room, 'South')
music_room.link_room(entrance_hall, 'North West')
utility_room.link_room(sun_room, 'West')
utility_room.link_room(shower_room, 'South')
shower_room.link_room(utility_room, 'North')
front_room.link_room(entrance_hall, 'West')
entrance_hall.link_room(front_room, 'East')
entrance_hall.link_room(music_room, 'South East')
entrance_hall.link_room(morning_room, 'South')
entrance_hall.link_room(cupboard_under_stairs, 'West')
entrance_hall.link_room(hall_stairs, 'Up')
entrance_hall.link_room(the_street, 'North')
hall_stairs.link_room(entrance_hall, 'Down')                           
cupboard_under_stairs.link_room(entrance_hall, 'East')
cupboard_under_stairs.link_room(cellar_stairs, 'Down')
cellar_stairs.link_room(cupboard_under_stairs, 'Up')
cellar_stairs.link_room(cellar, 'Down')                          
cellar.link_room(cellar_stairs, 'Up')                           



piano = Item('piano','Polished Rosewood Piano Forte')
#piano.describe()

dave = Enemy('Dave','A smelly zombie')
dave.set_conversation("Ugh, did din, I want to eat you")
dave.set_weakness(cheese)

daisy = Friend('Daisy','A lovely fairy')
daisy.set_conversation("oh what a handsome adventurer")
daisy.set_likes(['cheese','magic flute','rose'])

sigmund = Psychiatrist('Sigmund','A smartly dressed person wearing \n'
                       'a three piece suit and red polkadot bowtie \n'
                       'you look worried, maybe you should talk with him?')

music_room.set_character(dave)
kitchen.set_character(daisy)
front_room.set_character(sigmund)

backpack = {}
command_dictionary = {'?':'list valid commands', 'take item':'remove item from room and put in backpack',
                      'talk':'ask a character to talk','fight':'fight with character',
                      'give item':'give an item to a character','backpack':'lists backpack content'}

current_room = entrance_hall

while True:
    print("\n")
    current_room.get_details()
    if current_room.get_name() == 'The Street':
        print('end of game')
        break
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        inhabited = True
    else:
        inhabited = False
    command = input("> ")
    if command in ["North","South","East","West","South East","North West","Up","Down"]:   
        current_room = current_room.move(command)
    elif command == '?':
        for cmd, cmd_description  in sorted(command_dictionary.items()):
            print(cmd + ' : ' + cmd_description + "\n")
    elif command == 'backpack':
        for i in backpack.keys():
            print(i)
    elif command == 'take item':
        room_inventory = current_room.get_item_inventory().copy()
        if len(room_inventory) > 0 :
            for room_item_key in room_inventory.keys():
                if input("do you want the " + room_item_key + " Y/N ?") == 'Y':
                    room_item = current_room.get_item(room_item_key)
                    backpack[room_item.get_name()] = room_item
            print('backpack now contains ...')
            print(list(backpack.keys()))
        else:
            print("there is nothing to take here")
    elif command == "talk" and inhabited == True:
        inhabitant.talk()
    elif command == 'fight' and inhabited == True:
        weapon = input("what do you want to fight with? ")
        if weapon in backpack:   
            if inhabitant.fight(backpack[weapon]) == True:
                print("you survived")
            else:
                print("you died")
                break
        else:
            print('you do not have that item in your backpack')
    elif command == 'give item':
        if inhabitant.get_disposition() == "Friend":
            print('backpack contains ...')
            print(list(backpack.keys())) 
            gift = input("what do you want to give " + inhabitant.name + " ? ")
            
            if gift in backpack.keys():
                if gift in inhabitant.get_likes():
                    del backpack[gift]
                    print('backpack now contains.. ')
                    print(list(backpack.keys()))
                    inhabitant.display_affection()
                else:
                    print(inhabitant.get_name() + ' does not like the ' + gift)
            else:
                print('you do not have that item in your backpack')
        else:
            inhabitant.set_conversation('fight me you coward')
            inhabitant.talk()
    else:
        print("so what next?")



