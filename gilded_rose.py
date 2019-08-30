import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'items'))

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
                self.__update_sell_in(item)
                item.update_quality()

    def __update_sell_in(self,item):
        item.sell_in -= 1
