import unittest
import sys, os
sys.path.append(os.path.dirname(sys.path[0]))
from gilded_rose import *

class TestItem(unittest.TestCase):

    def test_conjured_item(self):
        c = Conjured(20,20)
        gr = GildedRose([c])
        gr.update_quality()
        self.assertEqual(c.quality,18)
        self.assertEqual(c.sell_in, 19)

    def test_gone_off_conjured_item(self):
        c = Conjured(0,20)
        gr = GildedRose([c])
        gr.update_quality()
        self.assertEqual(c.quality,16)
        self.assertEqual(c.sell_in, -1)
