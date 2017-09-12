class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        """initialises a character adding a name and description"""
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.disposition = None

    # Describe this character
    def describe(self):
        """describes a character"""
        print( self.name + " is here!" )
        print( self.description )
        print( self.disposition)

    def get_disposition(self):
        """used to tell friends from foes"""
        return self.disposition

    def get_name(self):
        """returns character's name"""
        return self.name

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        """sets text used when the Talk command is given to a character"""
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        """initiate conversation with character in same room """
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        """only enemies fight"""
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    
    def __init__(self, char_name, char_description):
        """ sub class of character """
        super().__init__(char_name, char_description)
        self.weakness = None
        self.disposition = "Foe"
        self.conversation = "How dare you"

    def set_weakness(self, weakness):
        """set weakness, used during combat """
        self.weakness = weakness

    def get_weakness(self):
        """weakness checked during combat """
        return self.weakness

    # Fight with this enemy
    def fight(self, combat_item):
        """combat with another character, if you lose you end the game """
        if combat_item == self.weakness:
            print("You fend off " + self.name + " with the " + combat_item.get_name())
            return True
        else:
            print('Alas ' + combat_item.get_name() + ' was ineffective')
            print(self.name + " crushes you, puny adventurer")
            return False
            
class Friend(Character):
    
    def __init__(self, char_name, char_description):
        """ sub class of character """
        super().__init__(char_name, char_description)
        self.likes = []
        self.disposition = "Friend"
        
    def get_likes(self):
        """shows what a character likes """
        return self.likes
    
    def set_likes(self,likelist):
        """stores a list of objects tha character likes """
        self.likes = likelist

    def display_affection(self):
        """to be extended...;) """
        print(self.name + " gives you a sloppy kiss!")

