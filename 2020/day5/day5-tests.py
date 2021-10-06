import unittest
import day5

class TestBspMethods(unittest.TestCase):

    def test_calculate_row_0(self):
        self.assertEqual(day5.calculate_row('FFFFFFFRRR'), 0)

    def test_calculate_row_127(self):
        self.assertEqual(day5.calculate_row('BBBBBBBRRR'), 127)

    def test_calculate_row_70(self):
        self.assertEqual(day5.calculate_row('BFFFBBFRRR'), 70)

    def test_calculate_row_14(self):
        self.assertEqual(day5.calculate_row('FFFBBBFRRR'), 14)

    def test_calculate_column_0(self):
        self.assertEqual(day5.calculate_column('FFFFFFFRRR'), 7)

    def test_calculate_column_0(self):
        self.assertEqual(day5.calculate_column('FFFFFFFLLL'), 0)

    def test_calculate_column_0(self):
        self.assertEqual(day5.calculate_column('FFFFFFFLRL'), 2)

    def test_seat_567(self):
        self.assertEqual(day5.calculate_seatid('BFFFBBFRRR'), 567)

    def test_seat_119(self):
        self.assertEqual(day5.calculate_seatid('FFFBBBFRRR'), 119)

    def test_seat_820(self):
        self.assertEqual(day5.calculate_seatid('BBFFBBFRLL'), 820)

    def test_highest_seat_820(self):
        cards = ['BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']
        self.assertEqual(day5.get_highest_seat_id(cards), 820)
    

if __name__ == '__main__':
    unittest.main()