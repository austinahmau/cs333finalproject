from operations import Operations

operations = []
operands1 = []
operands2 = []

file = open("input.txt", "r")
for line in file:
  #separates lines for the file to respective parts
  parts = line.strip().split()

  operations.append(parts[0])
  operands1.append(parts[1])
  operands2.append(parts[2])

file.close()

for i in range(len(operations)):
  calculations = Operations(operands1[i], operands2[i])

  if(operations[i] == "ADD"):
    result = calculations.bitwise_add(operands1[i], operands2[i])
    print("ADD: " + operands2[i] + " + " + operands1[i] + " = " + result)
    
  elif(operations[i] == "SUB"):
    result = calculations.bitwise_sub(operands1[i], operands2[i])
    print("SUB: " + operands2[i] + " - " + operands1[i] + " = " + result)
    
  elif(operations[i] == "NOT"):
    result = calculations.bitwise_not(operands1[i], operands2[i])
    print("NOT: " + operands1[i] + " = " + result)
    
  elif(operations[i] == "AND"):
    result = calculations.bitwise_and(operands1[i], operands2[i])
    print("AND: " + operands2[i] + " & " + operands1[i] + " = " + "0x" + result[2:].upper())
    
  elif(operations[i] == "ORR"):
    result = calculations.bitwise_orr(operands1[i], operands2[i])
    print("ORR: " + operands2[i] + " | " + operands1[i] + " = " + "0x" + result[2:].upper())
    
  elif(operations[i] == "XOR"):
    result = calculations.biwise_xor(operands1[i], operands2[i])
    print("XOR: " + operands2[i] + " ^ " + operands1[i] + " = " + "0x" + result[2:].upper())
    
  elif(operations[i] == "LSR"):
    result = calculations.bitwise_shift_right(operands1[i], operands2[i])
    print("LSR: " + operands1[i] + " << " + operands2[i] + " = " + "0x" + result[2:].upper())
    
  elif(operations[i] == "LSL"):
    result = calculations.bitwise_shift_left(operands1[i], operands2[i])
    print("LSL: " + operands1[i] + " >> " + operands2[i] + " = " + "0x" + result[2:].upper())

  else:
    print(operations[i] + " is not a valid command")