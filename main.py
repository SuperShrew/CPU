acc = 0
pc = 0
RAM = [0]*100

# 0 = store
# 1 = load acc
# 2 = input
# 3 = output
# 4 = add
# 5 = subtract
# 6 = branch if 0


def ALU(adr1, adr2, op):
  if op == 4:
    return adr1+adr2
  elif op == 5:
    return adr1-adr2

def CU(cmd):
  match cmd[0]:
    case 0:
      RAM[cmd[1:]] = acc

CU(011)
print(RAM)
