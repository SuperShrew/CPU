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
speed = 0.5

ram[99] = 80
ram[98] = 865
ram[97] = 868
ram[96] = 81
ram[95] = 883
ram[94] = 885
ram[93] = 866
ram[92] = 845

ram[0] = 299
ram[1] = 400
ram[2] = 298
ram[3] = 900
ram[4] = 297
ram[5] = 900
ram[6] = 297
ram[7] = 900
ram[8] = 292
ram[9] = 900
ram[10] = 296
ram[11] = 400
ram[12] = 295
ram[13] = 900
ram[14] = 294
ram[15] = 900
ram[16] = 293
ram[17] = 900

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
  global pc
  print("excecuting instruction", cmd)
  time.sleep(speed)
  match int(cmd[0]):
    case 1:
      #print(int(cmd[1:].lstrip("0")))
      print("storing", int(acc.lstrip("0")), "at address", int(cmd[1:].lstrip("0")))
      ram[int(cmd[1:].lstrip("0"))] = int(acc.lstrip("0"))
    case 2:
      print("loading accumulator with value", str(ram[int(cmd[1:].lstrip("0"))])[1:])
      acc = str(ram[int(cmd[1:].lstrip("0"))])[1:]
    case 3:
      print("awaiting input")
      acc = input("> ")
    case 4:
      print("outputting value", acc)
      output = output + acc + "\n"
    case 5:
      print("adding address", int(cmd[1:].lstrip("0")), "and accumulator value ", int(acc.lstrip("0")))
      acc = str(ALU(ram[int(cmd[1:].lstrip("0"))], int(acc.lstrip("0")), 5))
    case 6:
      print("subtracting address", int(cmd[1:].lstrip("0")), "and accumulator value ", int(acc.lstrip("0")))
      acc = str(ALU(ram[int(cmd[1:].lstrip("0"))], int(acc.lstrip("0")), 6))
    case 7:
      if ram[int(cmd[1:].lstrip("0"))] == 0:
        pc = int(cmd[1:])
        print("branching to address", cmd[1:])
      else:
        print("branch returned false, not branching")
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
    time.sleep(speed)
    CU(str(ram[pc]))
    print("-------------------------")
    print(output)
    pc+=1
    time.sleep(speed)
  print("program halted")


excecute()
