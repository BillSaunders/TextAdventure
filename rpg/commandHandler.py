# bill's CommandHandler class

class CommandHandler():
    
    def __init__(self, current_room, backpack):
        """ Deals with input commands"""
        self.valid_directions = ["North","South","East","West","South East","North West","Up","Down"]
        self.command_dictionary = {'?':'list valid commands', 'take item':'remove item from room and put in backpack',
                      'talk':'ask a character to talk','fight':'fight with character','describe':'describe current room', 
                      'give item':'give an item to a character','backpack':'lists backpack content'}
        self.current_room = current_room
        self.backpack = backpack
        self.room_occupant = current_room.get_character()



    def move(self, direction):
        self.current_room = self.current_room.move(direction)
        self.room_occupant = self.current_room.get_character()

    def take_room_item(self):
        room_inventory = self.current_room.get_item_inventory().copy()
        if len(room_inventory) > 0 :
            for room_item_key in room_inventory.keys():
                if input("do you want the " + room_item_key + " Y/N ?") == 'Y':
                    room_item = self.current_room.get_item(room_item_key)
                    self.backpack.add_item(room_item)
        else:
            print("there is nothing to take here")

    def display_commands(self):
        for cmd, cmd_description  in sorted(self.command_dictionary.items()):
            print(cmd + ' : ' + cmd_description + "\n")
        pass

    def fight(self):
        self.backpack.display_contents()
        weapon = input("what do you want to fight with? ")
        if weapon in self.backpack.get_item_keys():
            if self.room_occupant is not None:
                if self.room_occupant.fight(self.backpack.get_item(weapon)) == True:
                    print("you survived")
                    return True
                else:
                    print("you died")
                    return False
            else:
                print("there is nobody here to fight with")
                return True
        else:
            print(" you cannot fight without a weapon")
            return True

    def offer_gift(self):
        self.backpack.display_contents()
        gift_name = input("what item do you want to give ? ")
        if gift_name in self.backpack.get_item_keys():
            if self.room_occupant is not None:
                if self.room_occupant.accepts_gift(gift_name) == True:
                    self.room_occupant.set_held_item(self.backpack.remove_item(gift_name))
                else:
                    print('Your gift is rejected')             
            else:
                print('There is nobody here to receive your kind gift')
        else:
            print('you do not have that item in your backpack, so how can you offer it?')

    def ask_room_occupant_to_talk(self):
        if self.room_occupant is not None:
            self.room_occupant.talk()
        else:
            print("There is nobody here to talk with")

    def handle(self, command):
        if command in self.valid_directions :              
            self.move(command)
        elif command == '?':
            self.display_commands()
        elif command == 'backpack':
            self.backpack.display_contents()        
        elif command == 'take item':
            self.take_room_item()
        elif command == "talk":
            self.ask_room_occupant_to_talk()          
        elif command == "describe":
            self.current_room.describe()
        elif command == 'fight':
            if self.fight() == False:
                self.current_room = None
        elif command == 'give item':
            self.offer_gift()            
        else:
            print("so what next?")
        return self.current_room
