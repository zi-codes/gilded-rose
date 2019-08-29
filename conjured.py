from item import *

class Conjured(Item):

    def update_quality(self):
        if self.quality > 0:
            if self.sell_in > 0:
                self.quality = self.quality - 2
            else:
                self.quality = self.quality - 4
