import unittest
from backpack import Backpack
from item import Item
import sys
from io import StringIO
from unittest.mock import patch

class testBackpack(unittest.TestCase):

    """ setUpClass and tearDownClass run once at start and end """
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod    
    def tearDownClass(cls):
        print('tearDownClass')
        
    def check_printed_output(self,fakeOutput,expected_output,testcase_ref):
        """ utility method to compare captured output from method print statements to expected output"""
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, expected_output, msg=testcase_ref)    

    """ setUp and tearDown run for each test """
    def setUp(self):
        print('setUp creates backpack1, item1, item2 for tests')
        self.backpack1 = Backpack()
        self.item1 = Item('item1','item1_description')
        self.item2 = Item('item2','item2_description')
        self.backpack1.pack[self.item1.get_name()] = self.item1
        self.backpack1.pack[self.item2.get_name()] = self.item2
        self.assertTrue(len(self.backpack1.pack) == 2)
        
    def tearDown(self):
        print('tearDown sets backpack1, item1, item2 =  None,')
        print('\n')
        self.backpack1 = None
        self.item1 = None
        self.item2 = None
        
    
    def test_backpack_Constructor(self):
        print('test_backpack_Constructor starts')
        constructed_backpack = Backpack()
        self.assertEqual(constructed_backpack.pack,{})
        print('test_backpack_Constructor ends')

    def test_add_item(self):
        print('test_add_item() starts')
        backpack = self.backpack1
        item3 = Item('i3','i3_description')
        self.assertTrue(len(backpack.pack) == 2)
        backpack.add_item(item3)
        self.assertTrue(len(backpack.pack) == 3)
        self.assertTrue(backpack.pack['i3'] == item3)
        print('test_add_item() ends') 

    def test_remove_item(self):
        print('test_remove_item() starts')
        backpack = self.backpack1
        item2 = self.item2
        self.assertTrue(len(backpack.pack) == 2)
        backpack.remove_item(item2.get_name())
        self.assertTrue(len(backpack.pack) == 1)
        print('test_remove_item() ends')

    def test_display_contents(self):
        print('test_display_contents() starts')
        backpack = self.backpack1
        ## Stores output from print() in fakeOutput
        with patch('sys.stdout', new=StringIO()) as self.fakeOutput:
            backpack.display_contents()
        self.output = self.fakeOutput.getvalue().strip()
        expected ="backpack now contains ...\n['item1', 'item2']"
        self.assertEqual(self.output, expected)
        print('test_display_contents() ends')  
        
    def test_get_item(self):
        print('test_get_item() starts')
        backpack = self.backpack1
        returned_value = backpack.get_item('item1')
        self.assertEqual(returned_value, self.item1)
        self.assertTrue(len(backpack.pack) == 2)
        print('test_get_item() ends')
        
    def test_get_item_keys(self):
        print('test_get_item_keys() starts')
        backpack = self.backpack1
        self.assertEqual(sorted(backpack.get_item_keys()),['item1', 'item2'] )
        print('test_get_item_keys() ends')
        
    

if __name__ == '__main__':
    unittest.main()
