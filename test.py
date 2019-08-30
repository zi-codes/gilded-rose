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


# if __name__ == '__main__':
#     unittest.main()
