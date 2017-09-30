#Bill's backpack

class Backpack():
    def __init__(self):
        self.pack = {}
        
    def display_contents(self):
        print('backpack now contains ...')
        print(sorted(self.pack.keys()))

    def add_item(self, item):
        self.pack[item.get_name()] = item
        self.display_contents()  

    def remove_item(self, item_name):
        item = None
        if item_name in self.pack.keys():
            item = self.pack[item_name]
            del self.pack[item_name]
            self.display_contents()      
        return item

    def get_item_keys(self):
        return self.pack.keys()
              
    def get_item(self, item_name):
        if item_name in self.pack.keys():
            return self.pack[item_name]
        else:
            print('you do not have that item in your backpack')
            return False
