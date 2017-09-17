# bill's Item class

class Item():
    def __init__(self, item_name, item_description):
        """ constructs an Item and sets its name and description attributes"""
        self.name = item_name
        self.description = item_description
        
    def set_description(self, item_description):
        """ updates the description of the Item"""
        self.description = item_description

    def get_description(self):
        """ returns the description of the Item"""
        return self.description 
        
    def set_name(self, item_name):
        """ updates the name of the Item"""
        self.name = item_name

    def get_name(self):
        """ returns the name of the Item"""
        return self.name
        
    def describe(self):
        """ prints the item object's description """
        print(self.description)
