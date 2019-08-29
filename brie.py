from item import *

class Brie(Item):

    def update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
