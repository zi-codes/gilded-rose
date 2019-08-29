from item import *
from brie import *
from backstage_pass import *
from sulfuras import *
from conjured import *

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if type(item.sell_in) is int:
                self.update_sell_in(item)
                item.update_quality()

    def update_sell_in(self,item):
        item.sell_in = item.sell_in - 1
