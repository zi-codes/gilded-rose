import unittest
import sys
sys.path.append('/Users/student/tech_tests/gilded-rose')
from gilded_rose import *

class TestItem(unittest.TestCase):

        def test_sulfuras_is_constant(self):
            s = Sulfuras()
            gr = GildedRose([s])
            gr.update_quality()
            self.assertEqual(s.quality,80)
            self.assertEqual(s.sell_in, None)
