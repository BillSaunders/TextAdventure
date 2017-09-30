import unittest
from item import Item
import sys
from io import StringIO
from unittest.mock import patch

class testItem(unittest.TestCase):

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
        print('setUp creates item1 for tests')
        self.item1 = Item('TestItemName1','TestItemDescription1')
        
    def tearDown(self):
        print('tearDown sets item1 =  None,')
        print('\n')
        self.item1 = None
        
    
    def test_Item_Constructor(self):
        print('test_Item_Constructor starts')
        constructed_item = Item('ItemName','ItemDescription')
        self.assertEqual(constructed_item.name,'ItemName')
        self.assertEqual(constructed_item.description,'ItemDescription')
        print('test_Item_Constructor ends')

    def test_set_description(self):
        print('test_set_description() starts')
        testItem = self.item1
        testItem.set_description('new description')
        self.assertTrue(testItem.description == 'new description')
        print('test_set_description() ends') 

    def test_get_description(self):
        print('test_get_description() starts')
        item = self.item1
        self.assertEqual(item.description, item.get_description())
        print('test_get_description() ends')

    def test_describe(self):
        print('test_describe() starts')
        item = self.item1
        ## Stores output from print() in fakeOutput
        with patch('sys.stdout', new=StringIO()) as self.fakeOutput:
            item.describe()
        self.output = self.fakeOutput.getvalue().strip()
        expected ='TestItemDescription1'
        self.assertEqual(self.output, expected)
        print('test_describe() ends')  
        
    def test_set_name(self):
        print('test_set_name() starts')
        item = self.item1
        testname = 'testname1'
        item.set_name(testname)
        self.assertEqual(item.name, testname)
        print('test_set_name() ends')
        
    def test_get_name(self):
        print('test_get_name() starts')
        item = self.item1
        self.assertEqual(item.name, item.get_name())
        print('test_get_name() ends')
        
    

if __name__ == '__main__':
    unittest.main()
