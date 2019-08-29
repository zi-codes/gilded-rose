from item import *
from brie import *
from backstage_pass import *
from sulfuras import *
from conjured import *

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        self.update_sell_in_for_all()
        for item in self.items:
            if type(item.sell_in) is int:
                item.update_quality()

    def update_sell_in_for_all(self):
        for item in self.items:
            # this if statement will exclude sulfuras
            if type(item.sell_in) is int:
                item.sell_in = item.sell_in - 1
