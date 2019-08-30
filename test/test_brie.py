import unittest
import sys, os
sys.path.append(os.path.dirname(sys.path[0]))
from gilded_rose import *

class TestItem(unittest.TestCase):

    def test_brie(self):
        brie = Brie(20,20)
        gr = GildedRose([brie])
        gr.update_quality()
        self.assertEqual(brie.quality,21)
        self.assertEqual(brie.sell_in,19)

    def test_maxed_brie(self):
        brie = Brie(20,50)
        gr = GildedRose([brie])
        gr.update_quality()
        self.assertEqual(brie.quality,50)
        self.assertEqual(brie.sell_in,19)
