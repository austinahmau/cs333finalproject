import unittest
from converter import Converter
from operations import Operations

class TestOperations(unittest.TestCase):
  #integration tests
  def test_bitwise_add_integration(self):
    converter = Converter()
    converter.operand1 = "0x1"
    converter.operand2 = "0x1"
    operations = Operations(converter.operand1, converter.operand2)
    self.assertEqual(operations.bitwise_add(converter.operand1, converter.operand2), "0x2", "ADD should be 0x2")

  def test_bitwise_sub_integration(self):
    converter = Converter()
    converter.operand1 = "0x1"
    converter.operand2 = "0x1"
    operations = Operations(converter.operand1, converter.operand2)
    self.assertEqual(operations.bitwise_sub(converter.operand1, converter.operand2), "0x0", "SUB should be 0x0")

  def test_bitwise_not_integration(self):
    converter = Converter()
    converter.operand1 = "0x1"
    converter.operand2 = "0x1"
    operations = Operations(converter.operand1, converter.operand2)
    self.assertEqual(operations.bitwise_not(converter.operand1, converter.operand2), "-0x2", "NOT should be -0x2")

  def test_bitwise_and_integration(self):
    converter = Converter()
    converter.operand1 = "0x5"
    converter.operand2 = "0xA"
    operations = Operations(converter.operand1, converter.operand2)
    self.assertEqual(operations.bitwise_and(converter.operand1, converter.operand2), "0x0", "AND should be 0x0")

  def test_bitwise_orr_integration(self):
    converter = Converter()
    converter.operand1 = "0x5"
    converter.operand2 = "0xA"
    operations = Operations(converter.operand1, converter.operand2)
    self.assertEqual(operations.bitwise_orr(converter.operand1, converter.operand2), "0xf", "ORR should be 0xf")

  def test_biwise_xor_integration(self):
    converter = Converter()
    converter.operand1 = "0x5"
    converter.operand2 = "0xA"
    operations = Operations(converter.operand1, converter.operand2)
    self.assertEqual(operations.biwise_xor(converter.operand1, converter.operand2), "0xf", "XOR should be 0xf")

  def test_bitwise_shift_left_integration(self):
    converter = Converter()
    converter.operand1 = "0x2"
    converter.operand2 = "0x1"
    operations = Operations(converter.operand1, converter.operand2)
    self.assertEqual(operations.bitwise_shift_left(converter.operand1, converter.operand2), "0x4", "LSL should be 0x4")

  def test_bitwise_shift_right_integration(self):
    converter = Converter()
    converter.operand1 = "0x8"
    converter.operand2 = "0x1"
    operations = Operations(converter.operand1, converter.operand2)
    self.assertEqual(operations.bitwise_shift_right(converter.operand1, converter.operand2), "0x4", "LSR should be 0x4")
    