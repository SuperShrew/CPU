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
global log
log = []

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

showram = input("show ram? (enter = no, anything else = yes)\n> ")

def ALU(adr1, adr2, op):
  if op == 0:
    return adr1+adr2
  elif op == 1:
    return adr1-adr2

def CU(cmd):
  global acc
  global output
  global speed
  global pc
  global log
  #print("excecuting instruction", cmd)
  time.sleep(speed)
  match cmd[0:1]:
    case "01":
      #print(int(cmd[1:].lstrip("0")))
      #print("storing", int(acc), "at address", int(cmd[1:].lstrip("0")))
      ram[int(cmd[1:].lstrip("0"))] = int(acc)

def excecute():
  global pc
  while not(str(ram[pc]) == "#"):
    os.system("clear")
    print(str(ram[pc]))

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
    for a in range(0, len(i)):
      if i[a] == ";":
        i = i[:a]
        i = i.strip()
        break
    ram[x] = int(i)
    print(int(i))
    time.sleep(speed)
    x+=1
  input("press enter to excecute\n> ")

excecute()
