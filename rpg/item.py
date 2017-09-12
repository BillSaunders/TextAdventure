# bill's Item class

class Item():
    def __init__(self, item_name, item_description):
        self.name = item_name
        self.description = item_description
        
    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description 
        
    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name
        
    def describe(self):
        print(self.description)
