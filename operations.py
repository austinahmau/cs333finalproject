from converter import Converter


class Operations:

  def __init__(self, operand1, operand2):
    self.operand1 = operand1
    self.operand2 = operand2

  def bitwise_add(self, operand1, operand2):
    converter = Converter()
    binary1 = converter.hex_to_binary(operand1)
    binary2 = converter.hex_to_binary(operand2)
    bin_result = bin(int(binary2, 2) + (int(binary1, 2)))
    dec_result = int(bin_result, 2)
    return hex(dec_result)

  def bitwise_sub(self, operand1, operand2):
    converter = Converter()
    binary1 = converter.hex_to_binary(operand1)
    binary2 = converter.hex_to_binary(operand2)
    bin_result = bin(int(binary2, 2) - (int(binary1, 2)))
    dec_result = int(bin_result, 2)
    return hex(dec_result)

  def bitwise_not(self, operand1, operand2):
    converter = Converter()
    dec1 = converter.hex_to_decimal(operand1)    
    result = ~dec1
    return hex(result)

  def bitwise_and(self, operand1, operand2):
    converter = Converter()
    dec1 = converter.hex_to_decimal(operand1)
    dec2 = converter.hex_to_decimal(operand2)
    result = dec2 & dec1
    return hex(result)

  def bitwise_orr(self, operand1, operand2):
    converter = Converter()
    dec1 = converter.hex_to_decimal(operand1)
    dec2 = converter.hex_to_decimal(operand2)
    result = dec2 | dec1
    return hex(result)

  def biwise_xor(self, operand1, operand2):
    converter = Converter()
    dec1 = converter.hex_to_decimal(operand1)
    dec2 = converter.hex_to_decimal(operand2)
    result = dec2 ^ dec1
    return hex(result)

  def bitwise_shift_left(self, operand1, operand2):
    converter = Converter()
    dec1 = converter.hex_to_decimal(operand1)
    dec2 = converter.hex_to_decimal(operand2)
    result = dec1 << dec2
    return hex(result)

  def bitwise_shift_right(self, operand1, operand2):
    converter = Converter()
    dec1 = converter.hex_to_decimal(operand1)
    dec2 = converter.hex_to_decimal(operand2)
    result = dec1 >> dec2
    return hex(result)
