fh = open('23.txt', 'r')
program = []
for line in fh.readlines():
  line = line.strip()
  (cmd, args) = line.split(" ", 1)
  args = args.split(",")
  args = map(lambda s: s.strip(), args)
  if args[0][0] == '+' or args[0][0] == '-':
    args[0] = int(args[0])
  if len(args) > 1 and (args[1][0] == '+' or args[1][0] == '-'):
    args[1] = int(args[1])
  program.append((cmd, args))

ip = 0
registers = {"a": 0, "b":0}
while ip>=0 and ip < len(program):
  (cmd, args) = program[ip]
  if cmd == 'inc':
    registers[args[0]] += 1
  elif cmd == 'tpl':
    registers[args[0]] *= 3
  elif cmd == 'hlf':
    registers[args[0]] /= 2
  elif cmd == 'jio':
    if registers[args[0]] == 1:
      ip += args[1]
    else:
      ip += 1
  elif cmd == 'jie':
    if (registers[args[0]] % 2) == 0:
      ip += args[1]
    else:
      ip += 1
  elif cmd == 'jmp':
    ip += args[0]
    
  else:
    print "ERROR: " + cmd, args
  if cmd[0] != 'j':
    ip += 1

print registers

