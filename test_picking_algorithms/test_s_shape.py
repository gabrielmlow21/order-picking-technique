import unittest
from s_shape import s_shape_picking_technique

class TestSShape(unittest.TestCase):

    def test_s_shape_picking_technique(self):
        # Test cases for s_shape_picking_technique function
        self.assertEqual(s_shape_picking_technique([(0, 0)]), [(0, 0)])
        self.assertEqual(s_shape_picking_technique([(1, 1)]), [(1, 1)])
        self.assertEqual(s_shape_picking_technique([(0, 0), (3, 4)]), [(0, 0), (3, 4)])
        self.assertEqual(s_shape_picking_technique([(0, 0), (0, 1)]), [(0, 0), (0, 1)])
        self.assertEqual(s_shape_picking_technique([(0, 0), (1, 0), (2, 0)]), [(0, 0), (2, 0), (1, 0)])
        self.assertEqual(s_shape_picking_technique([(0, 0), (1, 1), (2, 2)]), [(0, 0), (2, 2), (1, 1)])
        self.assertEqual(s_shape_picking_technique([(0, 0), (1, 2), (3, 4), (5, 6)]), [(0, 0), (5, 6), (1, 2), (3, 4)])
        self.assertEqual(s_shape_picking_technique([(0, 0), (0, 1), (1, 1), (1, 0)]), [(0, 0), (1, 1), (0, 1), (1, 0)])
        self.assertEqual(s_shape_picking_technique([(0, 0), (2, 3), (5, 1), (4, 6)]), [(0, 0), (5, 1), (2, 3), (4, 6)])
        self.assertEqual(s_shape_picking_technique([(0, 0), (1, 1), (1, 2), (1, 3)]), [(0, 0), (1, 3), (1, 1), (1, 2)])

unittest.main()