from item import *

class Conjured(Item):

    def decrement(self):
        return 2 if self.sell_in > 0 else 4
