import unittest
from day12_pt2 import rotate_right, rotate_left

class TestShipMethods(unittest.TestCase):

    def test_rotate_right_E2S(self):
      waypoint = (1, 10)
      result = rotate_right(90, waypoint)
      north_south, east_west = result
      self.assertEqual(north_south, -10)
      self.assertEqual(east_west, 1)

    def test_rotate_right_S2W(self):
      waypoint = (-10, 1)
      result = rotate_right(90, waypoint)
      north_south, east_west = result
      self.assertEqual(north_south, -1)
      self.assertEqual(east_west, -10)

    def test_rotate_right_W2N(self):
      waypoint = (-1, -10)
      result = rotate_right(90, waypoint)
      north_south, east_west = result
      self.assertEqual(north_south, 10)
      self.assertEqual(east_west, -1)

    def test_rotate_right_N2E(self):
      waypoint = (10, -1)
      result = rotate_right(90, waypoint)
      north_south, east_west = result
      self.assertEqual(north_south, 1)
      self.assertEqual(east_west, 10)

    def test_rotate_left_E2N(self):
      waypoint = (1, 10)
      result = rotate_left(90, waypoint)
      north_south, east_west = result
      self.assertEqual(north_south, 10)
      self.assertEqual(east_west, -1)

    def test_rotate_left_N2W(self):
      waypoint = (10, -1)
      result = rotate_left(90, waypoint)
      north_south, east_west = result
      self.assertEqual(north_south, -1)
      self.assertEqual(east_west, -10)

    def test_rotate_left_W2S(self):
      waypoint = (-1, -10)
      result = rotate_left(90, waypoint)
      north_south, east_west = result
      self.assertEqual(north_south, -10)
      self.assertEqual(east_west, 1)

    def test_rotate_left_S2E(self):
      waypoint = (-10, 1)
      result = rotate_left(90, waypoint)
      north_south, east_west = result
      self.assertEqual(north_south, 1)
      self.assertEqual(east_west, 10)
