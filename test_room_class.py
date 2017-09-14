import unittest
from room import Room
from item import Item
from character import Character
##import sys
##from io import StringIO
##from contextlib import contextmanager

class testRoom(unittest.TestCase):

    """ setUpClass and tearDownClass run once at start and end """
    @classmethod
    def setUpClass(cls):
        print('setupClass')
##        cls.room = None
##        cls.item = None

    @classmethod    
    def tearDownClass(cls):
        print('tearDownClass')

##    @contextmanager
##    def capture(command, *args, **kwargs):
##        out, sys.stdout = sys.stdout, StringIO()
##        try:
##            command(*args, **kwargs)
##            sys.stdout.seek(0)
##            yield sys.stdout.read()
##        finally:
##            sys.stdout = out
        

    """ setUp and tearDown run for each test """
    def setUp(self):
        print('setUp creates room1, room2, item1, item2 for tests')
        self.room1 = Room('testRoom1')
        self.room2 = Room('testRoom2')
        self.item1 = Item('TestItemName1','TestItemDescription1')
        self.item2 = Item('TestItemName2','TestItemDescription2')
        self.character1 = Character('testCharName1','testCharDescription1')

    def tearDown(self):
        print('tearDown sets room1, room2, item1, item2  =  None,')
        print('\n')
        self.room1 = None
        self.room2 = None
        self.item1 = None
        self.item2 = None
        self.character1 = None
    
    def test_Room_Constructor(self):
        print('test_Room_Constructor starts')
        constructed_room = Room('constructedRoom')
        self.assertEqual(constructed_room.name,'constructedRoom')
        self.assertIsNone(constructed_room.description)
        self.assertEqual(len(constructed_room.linked_rooms),0)
        self.assertIsNone(constructed_room.character)
        self.assertTrue(len(constructed_room.inventory) == 0)
        print('test_Room_Constructor ends')

    def test_set_item(self):
        print('test_set_item() starts')
        room = self.room1
        testItem = self.item1
        room.set_item(testItem)
        self.assertTrue(room.inventory['TestItemName1'] == testItem)
        self.assertTrue(len(room.inventory) == 1)
        print('test_set_item() ends')

    def test_get_item(self):
        print('test_get_item() starts')
        room = self.room1
        item = self.item1
        room.inventory[item.get_name()] = item
        self.assertTrue(len(room.inventory) == 1)
        roomItem = room.get_item('TestItemName1')
        self.assertTrue(len(room.inventory) == 0)
        self.assertEqual(roomItem.name,'TestItemName1')
        self.assertEqual(roomItem.description,'TestItemDescription1')
        print('test_get_item() ends')

    def test_get_item_inventory(self):
        print('test_get_inventory() starts')
        room = self.room1
        # check inventory created empty by setUp
        self.assertTrue(len(room.inventory) == 0)
        item1 = self.item1
        item2 = self.item2
        # add two items to room
        room.inventory[item1.name] = item1
        room.inventory[item2.name] = item2
        inventory = room.get_item_inventory()
        # check that get_item_inventory returns these two item keys
        self.assertIn(item1.name, inventory)
        self.assertIn(item2.name, inventory)
        self.assertTrue(len(inventory) == 2)
        # check that get_item_inventory returns these two items 
        self.assertTrue(inventory['TestItemName1'] == item1)
        self.assertTrue(inventory['TestItemName2'] == item2)
        # check that get_item_inventory() did not change the room inventory size
        self.assertTrue(len(room.inventory) == 2)
        print('test_get_inventory() ends')

    def test_set_character(self):
        print('test_set_character() starts')
        room = self.room1
        char = self.character1
        room.set_character(char)
        self.assertEqual(room.character, char)
        print('test_set_character() ends')
    
    def test_get_character(self):
        print('test_get_character() starts')
        room = self.room1
        char = self.character1
        room.character = char
        self.assertEqual(room.character, room.get_character())
        print('test_get_character() ends')
        
    def test_set_description(self):
        print('test_set_description() starts')
        room = self.room1
        desc = 'text description of room'
        room.set_description(desc)
        self.assertEqual(room.description, desc)
        print('test_set_description() ends')
        
    def test_get_description(self):
        print('test_get_description() starts')
        room = self.room1
        room.description = 'text description of room'
        self.assertEqual(room.description, room.get_description())
        print('test_get_description() ends')
        
    def test_set_name(self):
        print('test_set_name() starts')
        room = self.room1
        testname = 'testname1'
        room.set_name(testname)
        self.assertEqual(room.name, testname)
        print('test_set_name() ends')
        
    def test_get_name(self):
        print('test_get_name() starts')
        room = self.room1
        self.assertEqual(room.name, room.get_name())
        print('test_get_name() ends')
        
    def test_link_room(self):
        print('test_link_room() starts')
        room1 = self.room1
        room2 = self.room2
        direction = 'NNE'
        room1.link_room(room2,direction)
        self.assertTrue(room1.linked_rooms[direction] == room2)
        self.assertIn(direction,room1.linked_rooms)
        print('test_link_room() ends')
        
    def test_move(self):
        print('test_move() starts')
        room1 = self.room1
        room2 = self.room2
        direction = 'NNE'
        otherDirection ='Fred'
        room1.linked_rooms[direction] =room2
        r2 = room1.move(direction)
        self.assertEqual(r2,room2)
        self.assertNotIn(otherDirection,room1.linked_rooms)
        r1 = room1.move(otherDirection)
        self.assertEqual(r1,room1)
        print('test_move() ends')
        
    def test_describe(self):
        print('test_describe() starts')
        print('still to be coded')
        print('test_describe() ends')
        pass
    def test_get_details(self):
        print('test_get_details() starts')
        print('still to be coded')
        print('test_get_details() ends')
        pass

if __name__ == '__main__':
    unittest.main()
