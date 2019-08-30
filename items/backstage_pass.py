from item import *

class BackstagePass(Item):

    def update_quality(self):
        if self.sell_in < 0:
            self.quality = 0
            return

        if self.quality < 50:
            if self.quality >= 0:
                self.quality -= self.decrement()

    def decrement(self):
        if self.sell_in > 10:
            return -1
        elif self.sell_in > 5:
            return -2
        else:
            return -3
