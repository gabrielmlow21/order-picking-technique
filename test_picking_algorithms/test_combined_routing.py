import unittest
import combined_routing

class TestCombinedRouting(unittest.TestCase):

    def test_calculate_distance(self):
        # Test cases for calculate_distance function
        self.assertEqual(combined_routing.calculate_distance((0, 0), (0, 0)), 0)
        self.assertEqual(combined_routing.calculate_distance((0, 0), (3, 4)), 7)
        self.assertEqual(combined_routing.calculate_distance((2, 3), (5, 7)), 7)
        self.assertEqual(combined_routing.calculate_distance((1, 1), (2, 2)), 2)
        self.assertEqual(combined_routing.calculate_distance((1, 1), (4, 5)), 7)
    
    def test_combined_routing(self):
        # Test cases for combined_routing function
        self.assertEqual(combined_routing.combined_routing([(0, 0)], True), [(0, 0)])
        self.assertEqual(combined_routing.combined_routing([(0, 0)], False), [(0, 0)])
        self.assertEqual(combined_routing.combined_routing([(1, 1)], True), [(1, 1)])
        self.assertEqual(combined_routing.combined_routing([(1, 1)], False), [(1, 1)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (1, 1)], True), [(0, 0), (1, 1)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (1, 1)], False), [(1, 1), (0, 0)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (3, 4)], True), [(0, 0), (3, 4)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (3, 4)], False), [(3, 4), (0, 0)])
        self.assertEqual(combined_routing.combined_routing([(1, 1), (2, 2)], True), [(1, 1), (2, 2)])
        self.assertEqual(combined_routing.combined_routing([(1, 1), (2, 2)], False), [(2, 2), (1, 1)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (1, 0), (2, 0)], True), [(0, 0), (2, 0), (1, 0)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (1, 0), (2, 0)], False), [(2, 0), (1, 0), (0, 0)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (1, 1), (2, 2)], True), [(0, 0), (2, 2), (1, 1)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (1, 1), (2, 2)], False), [(2, 2), (1, 1), (0, 0)])
        self.assertEqual(combined_routing.combined_routing([(1, 1), (3, 5), (2, 2)], True), [(1, 1), (3, 5), (2, 2)])
        self.assertEqual(combined_routing.combined_routing([(1, 1), (3, 5), (2, 2)], False), [(3, 5), (2, 2), (1, 1)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (1, 1), (2, 2), (3, 3)], True), [(0, 0), (3, 3), (2, 2), (1, 1)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (1, 1), (2, 2), (3, 3)], False), [(3, 3), (2, 2), (0, 0), (1, 1)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (1, 2), (3, 4), (5, 6)], True), [(0, 0), (5, 6), (3, 4), (1, 2)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (1, 2), (3, 4), (5, 6)], False), [(5, 6), (3, 4), (0, 0), (1, 2)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (0, 1), (1, 1), (1, 0)], True), [(0, 0), (1, 1), (0, 1), (1, 0)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (0, 1), (1, 1), (1, 0)], False), [(1, 1), (0, 1), (1, 0), (0, 0)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (2, 3), (5, 1), (4, 6)], True), [(0, 0), (4, 6), (2, 3), (5, 1)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (2, 3), (5, 1), (4, 6)], False), [(4, 6), (2, 3), (0, 0), (5, 1)])
        self.assertEqual(combined_routing.combined_routing([(0, 1), (2, 3), (4, 5), (6, 7)], False), [(6, 7), (4, 5), (0, 1), (2, 3)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (1, 1), (2, 2), (3, 3)], True), [(0, 0), (3, 3), (2, 2), (1, 1)])
        self.assertEqual(combined_routing.combined_routing([(0, 0), (1, 1), (2, 2), (3, 3)], False), [(3, 3), (2, 2), (0, 0), (1, 1)])



unittest.main()