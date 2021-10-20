import unittest
import day_18


class TestCalcMethods(unittest.TestCase):

  def test_evaluate_expression_1(self):
    self.assertEqual(3, day_18.calc_expression('1 + 2'))


  def test_evaluate_expression_2(self):
    self.assertEqual(6, day_18.calc_expression('2 * 3'))

  def test_evaluate_expression_3(self):
    self.assertEqual(71, day_18.calc_expression('1 + 2 * 3 + 4 * 5 + 6'))
  

  def test_infix_to_postfix_1_plus_2(self):
    result = day_18.infix_to_postfix('1 + 2')
    self.assertListEqual(['1', '2','+'], result)


  def test_infix_to_postfix_1_plus_2_times_3(self):
    result = day_18.infix_to_postfix('1 + 2 * 3')
    self.assertListEqual(['1', '2','+', '3', '*'], result)


  def test_infix_to_postfix_1_plus_2_times_3_parentesis(self):
    result = day_18.infix_to_postfix('1 + (2 * 3)')
    self.assertListEqual(['1', '2', '3', '*','+'], result)
