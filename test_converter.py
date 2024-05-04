import unittest
from converter import Converter

class TestConverter(unittest.TestCase):
  def test_hex_to_binary_conversion(self):
    converter = Converter()
    converter.operand1 = "0x1"
    converter.operand2 = "0x2"
    self.assertEqual(converter.hex_to_binary(converter.operand1), "00000001", "Conversion should be 00000001")
    self.assertEqual(converter.hex_to_binary(converter.operand2), "00000010", "Conversion should be 00000010")


  def test_hex_to_decimal_conversion(self):
    converter = Converter()
    converter.operand1 = "0x1"
    converter.operand2 = "0x2"
    self.assertEqual(converter.hex_to_decimal(converter.operand1), 1, "Conversion should be 1")
    self.assertEqual(converter.hex_to_decimal(converter.operand2), 2, "Conversion should be 2")