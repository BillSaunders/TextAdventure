import unittest
from item import Item
from character import Character, Enemy, Friend
import sys
from io import StringIO
from unittest.mock import patch


class testCharacter(unittest.TestCase):

    """ setUpClass and tearDownClass run once at start and end """
    @classmethod
    def setUpClass(cls):
        print('setupClass')
        

    @classmethod    
    def tearDownClass(cls):
        print('tearDownClass')

        

    """ setUp and tearDown run for each test """
    def setUp(self):
        print('setUp creates objects for tests')
        self.item1 = Item('TestItemName1','TestItemDescription1')
        self.character1 = Character('testCharName1','testCharDescription1')
        self.enemy1 = Enemy('testEnemyName1','testEnemyDescription1')
        self.friend1 = Friend('testFriendName1','testFriendDescription1')

    def tearDown(self):
        print('tearDown ')
        print('\n')
        self.item1 = None
        self.enemy1 = None
        self.friend1 = None
        self.character1 = None

    def check_printed_output(self,fakeOutput,expected_output,testcase_ref):
        """ utility method to compare captured output from method print statements to expected output"""
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, expected_output, msg=testcase_ref)
        
    
    def test_Character_Constructor(self):
        print('test_character_Constructor starts')
        constructed_character = Character('characterName','characterDescription')
        self.assertEqual(constructed_character.name,'characterName')
        self.assertEqual(constructed_character.description,'characterDescription')
        self.assertIsNone(constructed_character.conversation)
        self.assertIsNone(constructed_character.disposition)
        print('test_character_Constructor ends')

    def test_Enemy_Constructor(self):
        print('test_Enemy_Constructor starts')
        constructed_character = Enemy('characterName','characterDescription')
        self.assertEqual(constructed_character.name,'characterName')
        self.assertEqual(constructed_character.description,'characterDescription')
        self.assertEqual(constructed_character.conversation,'How dare you')
        self.assertEqual(constructed_character.disposition,'Foe')
        self.assertIsNone(constructed_character.weakness)
        print('test_Enemy_Constructor ends')

    def test_Friend_Constructor(self):
        print('test_Friend_Constructor starts')
        constructed_character = Friend('characterName','characterDescription')
        self.assertEqual(constructed_character.name,'characterName')
        self.assertEqual(constructed_character.description,'characterDescription')
        self.assertIsNone(constructed_character.conversation)
        self.assertEqual(constructed_character.disposition,'Friend')
        self.assertEqual(constructed_character.likes,[])
        print('test_Friend_Constructor ends')

    def test_describe(self):
        print('test_describe() starts')
        ## Stores output from print() in fakeOutput
        with patch('sys.stdout', new=StringIO()) as self.fakeOutput:
            self.character1.describe()
        self.output = self.fakeOutput.getvalue().strip()
        expected ='testCharName1 is here!\ntestCharDescription1\nNone'
        self.assertEqual(self.output, expected)
        print('test_describe() ends')
    

    def test_get_disposition(self):
        print('test_get_disposition() starts')
        self.assertEqual(self.character1.get_disposition(),
                         self.character1.disposition)
        print('test_get_disposition() ends')

    def test_get_name(self):
        print('test_get_name() starts')
        self.assertEqual(self.character1.name,
                         self.character1.get_name())
        print('test_get_name() ends')

    def test_set_conversation(self):
        print('test_set_conversation() starts')
        conv = 'test conversation, words, punctuation'
        self.character1.set_conversation(conv)
        self.assertEqual(self.character1.conversation, conv)
        print('test_set_conversation() ends')

    

    def test_talk(self):
        print('test_talk() starts')
        self.assertIsNone(self.character1.conversation)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.character1.talk()
        expected ="testCharName1 doesn't want to talk to you"
        self.check_printed_output(fakeOutput,expected,'test_talk1')
        
        self.character1.conversation = 'Test talk'
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.character1.talk()
        expected = '[testCharName1 says]: Test talk'
        self.check_printed_output(fakeOutput,expected,'test_talk2')
        print('test_talk() ends ')

    def test_fight(self):
        print('test_fight() starts')
        print('Try fight with Character instance')  
        #expect name doesn't want to fight with you, returns True
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertTrue(self.character1.fight(self.item1))
        expected ="testCharName1 doesn't want to fight with you"
        self.check_printed_output(fakeOutput,expected,'test_fight 1')
        
        print('Try fight with Friend instance')  
        #expect name doesn't want to fight with you. returns True
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertTrue(self.friend1.fight(self.item1))
        expected ="testFriendName1 doesn't want to fight with you" 
        self.check_printed_output(fakeOutput,expected,'test_fight 2')

        print('Try fight with Enemy instance')  
        #try to fight Enemy with no weakness
        #expect defeat = return False
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(self.enemy1.fight(self.item1))
        expected ='Alas TestItemName1 was ineffective\ntestEnemyName1 crushes you, puny adventurer'
        self.check_printed_output(fakeOutput,expected,'test_fight 3')
        
        #try to fight Enemy with weakness item1
        # expect victory = return True
        self.enemy1.weakness = self.item1
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertTrue(self.enemy1.fight(self.item1))
        expected ='You fend off testEnemyName1 with the TestItemName1'
        self.check_printed_output(fakeOutput,expected,'test_fight 4')
        print('test_fight() ends')
    
    def test_set_weakness(self):
        print('test_set_weakness() starts')
        weakness = 'testWeakness'
        self.enemy1.set_weakness(weakness)
        self.assertEqual(self.enemy1.weakness, weakness)
        print('test_set_weakness() ends')

    def test_get_weakness(self):
        print('test_get_weakness() starts')
        self.enemy1.weakness = 'testWeakness'
        self.assertEqual(self.enemy1.get_weakness(), 'testWeakness')
        print('test_get_weakness() ends')

        
        
    def test_get_likes(self):
        print('test_get_likes() starts')
        try:
            self.character1.likes = ['a','b']
        except AttributeError:
            print('expected this, Character does not have this attribute')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        self.friend1.likes = ['a','b']
        self.assertEqual(self.friend1.likes, self.friend1.get_likes())
        print('test_get_likes() ends')
        
    def test_set_likes(self):
        print('test_set_likes() starts')
        try:
            self.character1.set_likes(['a','b','c'])
        except AttributeError:
            print('expected this, Character does not have this method')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        self.friend1.set_likes(['a','b'])
        self.assertEqual(self.friend1.likes, ['a','b'])
        print('test_set_likes() ends')
        
    def test_display_affection(self):
        print('testdisplay_affection() starts')
        try:
            self.character1.display_affection()
        except AttributeError:
            print('expected this, Character does not have this method')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        
        try:
            self.enemy1.display_affection()
        except AttributeError:
            print('expected this, Enemy does not have this method')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.friend1.display_affection()
        expected ='testFriendName1 gives you a sloppy kiss!'
        self.check_printed_output(fakeOutput,expected,'test_display_affection')
        print('test_display_affection() ends')
        
    
if __name__ == '__main__':
    unittest.main()
