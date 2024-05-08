class Converter:
  def __init__(self):
    self.operand1 = ""
    self.operand2 = ""

  def hex_to_binary(self, hex_number):
    binary_number = bin(int(hex_number, 16))[2:].zfill(8)
    return binary_number

  def hex_to_decimal(self, hex_number):
    decimal_number = int(hex_number, 16)
    return decimal_number