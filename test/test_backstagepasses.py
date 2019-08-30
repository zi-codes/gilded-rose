import unittest
import sys, os
sys.path.append(os.path.dirname(sys.path[0]))
from gilded_rose import *

class TestItem(unittest.TestCase):

    def test_normal_pass(self):
        backstage_pass = BackstagePass(20,20)
        gr = GildedRose([backstage_pass])
        gr.update_quality()
        self.assertEqual(backstage_pass.quality,21)
        self.assertEqual(backstage_pass.sell_in,19)

    def test_pass_10_days(self):
        backstage_pass = BackstagePass(10,20)
        gr = GildedRose([backstage_pass])
        gr.update_quality()
        self.assertEqual(backstage_pass.quality,22)
        self.assertEqual(backstage_pass.sell_in,9)

    def test_pass_5_days(self):
        backstage_pass = BackstagePass(5,20)
        gr = GildedRose([backstage_pass])
        gr.update_quality()
        self.assertEqual(backstage_pass.quality,23)
        self.assertEqual(backstage_pass.sell_in,4)

    def test_pass_on_concert_day(self):
        backstage_pass = BackstagePass(1,20)
        gr = GildedRose([backstage_pass])
        gr.update_quality()
        self.assertEqual(backstage_pass.quality,23)
        self.assertEqual(backstage_pass.sell_in,0)

    def test_pass_after_concert(self):
        backstage_pass = BackstagePass(0,20)
        gr = GildedRose([backstage_pass])
        gr.update_quality()
        self.assertEqual(backstage_pass.quality,0)
        self.assertEqual(backstage_pass.sell_in,-1)
