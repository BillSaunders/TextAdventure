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
                        'There is bread baking in the oven and some sort of curry \n'
                        'simmering on the hob in a volcanic orange cast iron pot...\n'
                        'The ivory coloured tiles on the walls reflect the light that \n'
                        'streams in from the garden window. \n'
                        'The tiled floor feels cool under your bare feet \n')
kitchen.set_item(magic_kettle)
kitchen.set_item(cheese)
entrance_hall = Room('Entrance Hall')
entrance_hall.set_description('A long hallway which has doors leading off it and \n'
                              'a staircase that goes up to the first floor.\n'
                              'A sign by the door asks politely that you remove your shoes.. you comply. \n'
                              'There are exotic ornaments adorning the walls, \n'
                              'a terracotta mask from Mexico, \n' 
                              'a polished tin plate from India,\n'
                              'a small colourful metal tray from Turkey...\n'
                              'numerous framed pictures...\n'
                              'A dark green jade turtle from Hong Kong shimmers on the telephone table \n'
                              'by the front door. Its surface smooth and sensual to the touch. \n'
                              'Whoever acquired this piece has exquisite (and expensive) taste')
front_room = Room('Front room')
front_room.set_description('a handsome room with large marble fireplace and bay window.\n'
                           'The carpet is green and the walls beige. \n'
                           'There is a cream coloured chaise longue in one corner, opposite to it,\n'
                           'against the far wall a large commfortable gold and black chesterfield \n'
                           'with soft cushions that silently invites you to rest your weary limbs for a while. \n'
                           'On the mantlepiece above the fireplace is a hand crafted soapstone seal from Canada, \n'
                           'about six inches in length. Next to it a circular sandpicture ten inches or so across, \n'
                           'the threads of coloured sand are still in motion,  indicating it was turned recently. \n'
                           'On the hearth lie six dark wooden frogs from Malaysia and an assortment of beautiful shells... \n'
                           'cowries, cone shells and a white conch shell turned to display its delicate pink interior.')
music_room = Room('Music room')
music_room.set_description("white walls, a large mirror above a small upright rosewood piano.\n"
                           "There are bookshelves along the far wall and a rocking chair in the corner.\n"
                           "The books are eclectic, several physics textbooks, paperback editions of the \n"
                           "iliad and the odyssey, Plato's republic, Dostoevsky's crime and punishment,  \n"
                           "tomes on various aspects of Chess, Karl Popper's conjectures and refutations, \n"
                           "a 1980 copy of the encyclopedia Britannica...\n"
                           "In the centre of the room under a black chandelier is a large antique table \n"
                           "with six robust wooden chairs.")
music_room.set_item(magic_flute)
morning_room = Room('Morning room')
morning_room.set_description('a light and airy room, with teracotta coloured wallpaper \n'
                             'a low 1960s wooden cabinet contains bottles of coloured liquids, \n'
                             'possibly for making cocktails! \n'
                             'The floor is polished wood and there are cupboards containing wine glasses, \n'
                             'beer glasses, china plates and cups, tea pots of varous design...  ')
morning_room.set_item(flower)
sun_room = Room('Sun room')
sun_room.set_description('Large windows and double door to the garden. \n'
                         'A comfortable room with polished wooden floor, \n'
                         'walls are yellow and woodwork orange in colour. Indoor plants \n'
                         'seem to thrive here. A dark blue glass charm to ward away the evil eye hangs \n'
                         'from the top rail of one window frame')
sun_room.set_item(banana)
sun_room.set_item(cheese)
sun_room.set_item(magic_flute)
utility_room = Room('utility room')
utility_room.set_description('A simple sink, washing machine, and dryer are here. \n'
                             'The tiled walls and floor give a cool feel to the room. \n'
                             'You catch sight of your reflection in the small octagonal mirror above the sink, \n'
                             'you cannot help smiling at the familiar friendly face looking back at you.')
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
cellar_stairs.set_description('dark and narrow stairs leading downward, \n'
                                        'the ancient wooden treads of the stair creak under foot \n'
                                        'betraying your presence to whatever is below in the darkness...')
cellar = Room('Cellar')
cellar.set_description('it is too dark to see but strange groaning sounds \n'
                       'filter through the darkness, it is cold and scary. \n'
                       'You strike a match... there is a brief glimmer of light reflected \n'
                       'from a row of glass demijohns, but the match goes out before your eyes \n'
                       'can adjust properly to the dim glow. It was your last match...')                          
hall_stairs = Room('Hall Stairs')
hall_stairs.set_description('A Victorian staircase with polished wooded spindrels and \n'
                            'hand rail leading up and around.')
the_street = Room('The Street')
the_street.set_description('You leave the house and find yourself back \n'
                           'in the street. Farewell brave adventurer \n'
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
                      'talk':'ask a character to talk','fight':'fight with character','describe':'describe current room', 
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
    elif command == "describe":
        current_room.describe()
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



