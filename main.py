import time
import os

global acc
acc = 0
global pc
pc = 0
global ram
ram = [0]*16384
global output
output = ""
global speed
speed = 1

# 1 = store
# 2 = load acc
# 3 = input
# 4 = output
# 5 = add
# 6 = subtract
# 7 = branch if 0
# 8 = data
# 9 = ascii value output
# # = halt program


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
      print("storing", int(acc), "at address", int(cmd[1:].lstrip("0")))
      ram[int(cmd[1:].lstrip("0"))] = int(acc)
    case 2:
      print("loading accumulator with value", str(ram[int(cmd[1:].lstrip("0"))]))
      acc = str(ram[int(cmd[1:].lstrip("0"))])
    case 3:
      print("awaiting input")
      acc = input("> ")
    case 4:
      print("outputting value", acc)
      output = output + str(acc) + "\n"
    case 5:
      print("adding address", int(cmd[1:].lstrip("0")), "and accumulator value ", int(acc.lstrip("0")))
      acc = str(ALU(ram[int(cmd[1:].lstrip("0"))], int(acc.lstrip("0")), 5))
    case 6:
      print("subtracting address", int(cmd[1:].lstrip("0")), "and accumulator value ", int(acc.lstrip("0")))
      acc = str(ALU(ram[int(cmd[1:].lstrip("0"))], int(acc.lstrip("0")), 6))
    case 7:
      print(cmd[1:3])
      print(ram[int(cmd[1:5].lstrip("0"))])
      if ram[int(cmd[1:5].lstrip("0"))] == 0:
        pc = int(cmd[4:])
        print("branching to address", cmd[3:])
      else:
        print("branch returned false, not branching")
    case 8:
      print("defined data:", int(cmd[1:].lstrip("0")), "| assigning to accumulator")
      acc = str(cmd[1:].lstrip("0"))
    case 9:
      print("outputting ascii value", int(acc), chr(int(acc)))
      output = output + chr(int(acc)) + "\n"

def excecute():
  global pc
  while not(str(ram[pc]) == "#"):
    os.system("clear")
    print(str(ram[pc]))
    print(ram)
    print(pc)
    print("-------------------------")
    print(output)
    print("-------------------------")
    print("fetching instruction")
    time.sleep(speed)
    CU(str(ram[pc]))
    pc+=1
    time.sleep(speed)
  os.system("clear")
  print(ram)
  print(pc)
  print("-------------------------")
  print(output)
  print("-------------------------")
  print("program halted")

with open("code.txt", "r+") as f:
  print("compiling...")
  x = 0
  for i in f.readlines():
    if i[0] == "!":
      speed = float(i[1:])
      continue
    if i.replace("\n", "") == "":
      ram[x] = 0
      x+=1
      continue
    if i.replace("\n", "") == "#":
      ram[x] = "#"
      print("#")
      x+=1
      continue
    ram[x] = int(i)
    print(int(i))
    time.sleep(0.1)
    x+=1
  input("press enter to excecute\n> ")

excecute()
