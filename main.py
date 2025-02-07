import time
import os

global acc
acc = 0
global pc
pc = 0
global ram
ram = [0]*100
global output
output = ""
global speed
speed = 3

ram[0] = 300
ram[1] = 199
ram[2] = 400
ram[3] = 845
ram[4] = 900
ram[5] = 268
ram[6] = 400
ram[68] = 137
# 1 = store
# 2 = load acc
# 3 = input
# 4 = output
# 5 = add
# 6 = subtract
# 7 = branch if 0
# 8 = data
# 9 = ascii value output


def ALU(adr1, adr2, op):
  if op == 5:
    return adr1+adr2
  elif op == 6:
    return adr1-adr2

def CU(cmd):
  global acc
  global output
  global speed
  print("excecuting instruction", cmd)
  time.sleep(speed/4)
  match int(cmd[0]):
    case 1:
      #print(int(cmd[1:].lstrip("0")))
      print("storing", int(acc.lstrip("0")), "at address", int(cmd[1:].lstrip("0")))
      ram[int(cmd[1:].lstrip("0"))] = int(acc.lstrip("0"))
    case 2:
      print("loading accumulator with value", str(ram[int(cmd[1:].lstrip("0"))]))
      acc = str(ram[int(cmd[1:].lstrip("0"))])
    case 3:
      print("awaiting input")
      acc = input("> ")
    case 4:
      print("outputting value", acc)
      output = output + acc + "\n"
    case 5:
      print("adding address", int(cmd[1:].lstrip("0")), "and accumulator value ", int(acc.lstrip("0")))
      acc = ALU(ram[int(cmd[1:].lstrip("0"))], int(acc.lstrip("0")), 5)
    case 6:
      print("subtracting address", int(cmd[1:].lstrip("0")), "and accumulator value ", int(acc.lstrip("0")))
      acc = ALU(ram[int(cmd[1:].lstrip("0"))], int(acc.lstrip("0")), 6)
    case 8:
      print("arbitrary data:", int(cmd[1:].lstrip("0")), "| assigning to accumulator")
      acc = str(cmd[1:].lstrip("0"))
    case 9:
      print("outputting ascii value", int(acc), chr(int(acc)))
      output = output + chr(int(acc)) + "\n"
def excecute():
  global pc
  while not(str(ram[pc]) == "0"):
    os.system("clear")
    print(ram)
    print(pc)
    print("fetching instruction")
    time.sleep(speed/4)
    CU(str(ram[pc]))
    print("-------------------------")
    print(output)
    pc+=1
    time.sleep(speed)


excecute()
