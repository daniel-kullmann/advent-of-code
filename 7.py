import re

lines = dict()
gates = dict()

class Line:
  def __init__(self, name, value=None):
    self.name = name
    self.value = value
    self.changed = value != None
  def set(self,value):
    if self.value != value:
      self.changed = True
    self.value = value
  def __repr__(self):
    return "(" + self.name + ": " + str(self.value) + " " + str(self.changed) + ")"
  
class Constant:
  def __init__(self,value, output):
    self.inputs = []
    self.output = output
    self.value = value
  def get(self):
    return self.value
  def evaluate(self):
    #print "CONST: -> " + self.output + " " + str(self.value)
    lines[self.output].set(self.value)
  def __repr__(self):
    return "CONST " + self.value

class NotGate:
  def __init__(self,input, output):
    self.inputs = [input]
    self.output = output
  def get(self):
    return lines[self.output]
  def evaluate(self):
    if lines[self.inputs[0]].value == None: return
    lines[self.output].set(~lines[self.inputs[0]].value)
    #print "NOT: " + str(self.inputs[0]) + " " + str(lines[self.inputs[0]].value) + " " + str(~lines[self.inputs[0]].value) + " -> " + self.output + " " + str(lines[self.output].value)
  def __repr__(self):
    return "NOT " + self.inputs[0]

class PassGate:
  def __init__(self,input, output):
    self.inputs = [input]
    self.output = output
  def get(self):
    return lines[self.output]
  def evaluate(self):
    if lines[self.inputs[0]].value == None: return
    lines[self.output].set(lines[self.inputs[0]].value)
    #print "PASS: " + str(self.inputs[0]) + " -> " + self.output + " " + str(lines[self.output].value)
  def __repr__(self):
    return "PASS " + self.inputs[0]

class BinaryGate:
  def __init__(self, input1, input2, output):
    self.inputs = [input1, input2]
    self.output = output
  def get(self):
    return lines[self.output]

class AndGate(BinaryGate):
  def evaluate(self):
    if lines[self.inputs[0]].value == None or lines[self.inputs[1]].value == None: return
    lines[self.output].set(lines[self.inputs[0]].value & lines[self.inputs[1]].value)
    #print "AND: " + str(self.inputs[0]) + ", " + str(self.inputs[1]) + " -> " + self.output + " " + str(lines[self.output].value)
  def __repr__(self):
    return "AND " + self.inputs[0] + " " + self.inputs[1]

class OrGate(BinaryGate):
  def evaluate(self):
    if lines[self.inputs[0]].value == None or lines[self.inputs[1]].value == None: return
    lines[self.output].set(lines[self.inputs[0]].value | lines[self.inputs[1]].value)
    #print "OR: " + str(self.inputs[0]) + ", " + str(self.inputs[1]) + " -> " + self.output + " " + str(lines[self.output].value)
  def __repr__(self):
    return "OR " + self.inputs[0] + " " + self.inputs[1]

class LShiftGate(BinaryGate):
  def evaluate(self):
    if lines[self.inputs[0]].value == None or lines[self.inputs[1]].value == None: return
    lines[self.output].set(lines[self.inputs[0]].value << lines[self.inputs[1]].value)
    #print "LS: " + str(self.inputs[0]) + ", " + str(self.inputs[1]) + " -> " + self.output + " " + str(lines[self.output].value)
  def __repr__(self):
    return "LS " + self.inputs[0] + " " + self.inputs[1]

class RShiftGate(BinaryGate):
  def evaluate(self):
    if lines[self.inputs[0]].value == None or lines[self.inputs[1]].value == None: return
    lines[self.output].set(lines[self.inputs[0]].value >> lines[self.inputs[1]].value)
    #print "RS: " + str(self.inputs[0]) + ", " + str(self.inputs[1]) + " -> " + self.output + " " + str(lines[self.output].value)
  def __repr__(self):
    return "RS " + self.inputs[0] + " " + self.inputs[1]

number = re.compile("[0-9]+")
constantOp = re.compile("([a-z]+|[0-9]+) -> ([a-z]+)")
unaryOp = re.compile("(NOT) ([a-z]+) -> ([a-z]+)")
binaryOp = re.compile("([a-z]+|[0-9]+) (AND|OR|LSHIFT|RSHIFT) ([a-z]+|[0-9]+) -> ([a-z]+)")


fh = open('7.txt', 'r')
for line in fh.readlines():
  line = line.strip()
  mc = constantOp.match(line)
  mu = unaryOp.match(line)
  mb = binaryOp.match(line)
  if mc:
    input = mc.group(1)
    output = mc.group(2)
    if number.match(input):
      lines[input] = Line(input, int(input))
      lines[output] = Line(output, int(input))
      gates[output] = Constant(int(input), output)
    else:
      lines[output] = Line(output)
      gates[output] = PassGate(input, output)
  elif mu:
    op = mu.group(1) 
    input = mu.group(2)
    output = mu.group(3)
    lines[output] = Line(output)
    gates[output] = NotGate(input, output)
  elif mb:
    op = mb.group(2) 
    input1 = mb.group(1)
    input2 = mb.group(3)
    if number.match(input1):
      lines[input1] = Line(input1, int(input1))
    if number.match(input2):
      lines[input2] = Line(input2, int(input2))
    output = mb.group(4)
    lines[output] = Line(output)
    if op == 'AND':
      gates[output] = AndGate(input1, input2, output)
    elif op == 'OR':
      gates[output] = OrGate(input1, input2, output)
    elif op == 'LSHIFT':
      gates[output] = LShiftGate(input1, input2, output)
    elif op == 'RSHIFT':
      gates[output] = RShiftGate(input1, input2, output)
    else:
      print ("ERROR: " + line)
  else:
    print ("ERROR: " + line)

def findChangedLines(lines):
    changedLines = [line for line in lines.values() if line.changed]
    for line in changedLines:
      line.changed = False
    return changedLines

def isIn(inputs, expecteds):
  for input in inputs:
    for expected in expecteds:
      if input == expected: 
        return True
  return False

def findGatesToFire(lineNames):
  gatesToFire = [gate for gate in gates.values() if isIn(gate.inputs, lineNames)]
  return gatesToFire

#print "\n".join([key + ": " + str(lines[key]) for key in sorted(lines.keys())])

print len(gates.values())
for i in range(0,1000):
  for gate in gates.values(): 
    gate.evaluate()
  print(lines['a'])




