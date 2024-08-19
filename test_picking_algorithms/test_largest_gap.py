import unittest
from largest_gap import largest_gap_picking_tecnnique

class TestLatgestGap(unittest.TestCase):
    
    def test_largest_gap_picking_tecnnique(self):
        # Test cases for largest_gap function
        self.assertEqual(largest_gap_picking_tecnnique([(0, 0)]), [(0, 0)])
        self.assertEqual(largest_gap_picking_tecnnique([(1, 1)]), [(1, 1)])
        self.assertEqual(largest_gap_picking_tecnnique([(0, 0), (1, 1)]), [(1, 1), (0, 0)])
        self.assertEqual(largest_gap_picking_tecnnique([(0, 0), (3, 4)]), [(3, 4), (0, 0)])
        self.assertEqual(largest_gap_picking_tecnnique([(2, 2), (3, 4)]), [(3, 4), (2, 2)])
        self.assertEqual(largest_gap_picking_tecnnique([(0, 0), (1, 0), (2, 0)]), [(1, 0), (2, 0), (0, 0)])
        self.assertEqual(largest_gap_picking_tecnnique([(1, 1), (2, 2), (3, 3)]), [(2, 2), (3, 3), (1, 1)])
        self.assertEqual(largest_gap_picking_tecnnique([(1, 1), (3, 5), (2, 2)]), [(3, 5), (1, 1), (2, 2)])
        self.assertEqual(largest_gap_picking_tecnnique([(0, 0), (1, 2), (3, 4), (5, 6)]), [(3, 4), (5, 6), (0, 0), (1, 2)])
        self.assertEqual(largest_gap_picking_tecnnique([(0, 0), (0, 1), (1, 1), (1, 0)]), [(1, 0), (1, 1), (0, 0), (0, 1)])
        self.assertEqual(largest_gap_picking_tecnnique([(0, 0), (2, 3), (5, 1), (4, 6)]), [(5, 1), (0, 0), (2, 3), (4, 6)])
        self.assertEqual(largest_gap_picking_tecnnique([(0, 0), (1, 1), (2, 2), (3, 3)]), [(1, 1), (2, 2), (3, 3), (0, 0)])
        self.assertEqual(largest_gap_picking_tecnnique([(1, 1), (2, 2), (3, 3), (4, 4)]), [(2, 2), (3, 3), (4, 4), (1, 1)])
        self.assertEqual(largest_gap_picking_tecnnique([(1, 1), (2, 2), (4, 4), (7, 7)]), [(7, 7), (1, 1), (2, 2), (4, 4)])

unittest.main()