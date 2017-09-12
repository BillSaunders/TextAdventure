# bill's Room class

class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.inventory = {}
        
    def set_item(self, room_item):
        self.inventory[room_item.get_name()] = room_item

    def get_item(self, room_item_key):
        room_item = self.inventory[room_item_key]
        del self.inventory[room_item_key]
        return room_item

    def  get_item_inventory(self):
        return self.inventory

    def set_character(self, room_character):
        self.character = room_character

    def get_character(self):
        return self.character
    
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description 
        
    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name
        
    def describe(self):
        print(self.description)
        if self.inventory is not None:
            for room_item in self.inventory.keys():
             print("there is a " + room_item + ' here')
        else:
            print("the room is empty of portable items")
    
    def link_room(self,  room_to_link_to, direction):
        self.linked_rooms[direction] = room_to_link_to
        
    def get_details(self):
        print('You are in the ' + self.get_name())
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print('The '+ room.get_name() + ' is ' + direction)
        
    def move(self,  direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
