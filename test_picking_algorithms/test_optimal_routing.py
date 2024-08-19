import unittest
from optimal_routing import optimal_routing

class TestOptimalRouting(unittest.TestCase):

    def test_optimal_routing(self):
        # Test cases for optimal_routing function
        self.assertEqual(optimal_routing([(0, 0)]), [(0, 0)])
        self.assertEqual(optimal_routing([(1, 1)]), [(1, 1)])
        self.assertEqual(optimal_routing([(0, 0), (0, 1)]), [(0, 0), (0, 1)])
        self.assertEqual(optimal_routing([(0, 0), (3, 4)]), [(0, 0), (3, 4)])
        self.assertEqual(optimal_routing([(0, 0), (1, 0), (2, 0)]), [(0, 0), (1, 0), (2, 0)])
        self.assertEqual(optimal_routing([(0, 0), (0, 1), (0, 2)]), [(0, 0), (0, 1), (0, 2)])
        self.assertEqual(optimal_routing([(0, 0), (1, 2), (3, 4), (5, 6)]), [(0, 0), (1, 2), (3, 4), (5, 6)])
        self.assertEqual(optimal_routing([(0, 0), (0, 1), (1, 1), (1, 0)]), [(0, 0), (0, 1), (1, 1), (1, 0)])
        self.assertEqual(optimal_routing([(0, 0), (2, 3), (5, 1), (4, 6)]), [(0, 0), (2, 3), (5, 1), (4, 6)])
        self.assertEqual(optimal_routing([(0, 0), (0, 1), (0, 2), (0, 3)]), [(0, 0), (0, 1), (0, 2), (0, 3)])

unittest.main()
