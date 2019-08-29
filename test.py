import unittest
from gilded_rose import *

class TestItem(unittest.TestCase):

    def test_normal_item(self):
        item = Item(20,20)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.quality,19)
        self.assertEqual(item.sell_in,19)

    def test_gone_off_item(self):
        item = Item(0,20)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.quality,18)
        self.assertEqual(item.sell_in,-1)

    def test_quality_cannot_sink_below_zero(self):
        item = Item(0,0)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.quality,0)
        self.assertEqual(item.sell_in,-1)

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

    def test_pass_after_concert(self):
        backstage_pass = BackstagePass(0,20)
        gr = GildedRose([backstage_pass])
        gr.update_quality()
        self.assertEqual(backstage_pass.quality,0)
        self.assertEqual(backstage_pass.sell_in,-1)

    def test_sulfuras_is_constant(self):
        s = Sulfuras()
        gr = GildedRose([s])
        gr.update_quality()
        self.assertEqual(s.quality,80)
        self.assertEqual(s.sell_in, None)

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

if __name__ == '__main__':
    unittest.main()
