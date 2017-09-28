# bill's Room class

class Room():
    def __init__(self, room_name):
        """ Constructor sets the name of the room and initialises other attributes"""
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.inventory = {}
        self.first_time_here = True
        
    def set_item(self, room_item):
        """ adds an Item to the room's inventory using the Item name as the key"""
        self.inventory[room_item.get_name()] = room_item

    def get_item(self, room_item_key):
        """ retrieves an Item from the inventory using the key supplied
    deletes the Item from the inventory
    and returns an Item """
        room_item = self.inventory[room_item_key]
        del self.inventory[room_item_key]
        return room_item

    def  get_item_inventory(self):
        """ returns the room inventory """
        return self.inventory

    def set_character(self, room_character):
        """ adds a character to the room """
        self.character = room_character

    def get_character(self):
        """ returns the character that is in the room"""
        return self.character
    
    def set_description(self, room_description):
        """ updates the room description attribute """
        self.description = room_description

    def get_description(self):
        """ returns the room description """
        return self.description 
        
    def set_name(self, room_name):
        """ updates the room name"""
        self.name = room_name

    def get_name(self):
        """ returns the room name """
        return self.name
        
    def describe(self):
        """ prints the description
        lists out any Items held in the room inventory"""
        print(self.description)
        self.first_time_here = False
        if self.inventory is not None:
            for room_item in self.inventory.keys():
             print("there is a " + room_item + ' here')
        else:
            print("the room is empty of portable items")
    
    def link_room(self,  room_to_link_to, direction):
        """ adds link to the next room using the direction as the key"""
        self.linked_rooms[direction] = room_to_link_to
        
    def get_details(self):
        """ tells you where you are 
        invokes the self.describe method 
        tells you about any linked rooms and their direction"""
        print('You are in the ' + self.get_name())
        if self.first_time_here == True:
            self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print('The '+ room.get_name() + ' is ' + direction)
        
    def move(self,  direction):
        """ if a valid direction is input, returns the linked room
        otherwise, outputs a message and returns the current room"""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
