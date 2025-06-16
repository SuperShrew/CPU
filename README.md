HOW TO USE:

at the start of your code file use a ! and a number to define the time it takes in seconds to do part of a cycle (this is not necassary and is automatically set to 1)

also just so you know if you have used the ! at the start, the ram address you are storing your instruction in is line number - 2, if not it is line number - 1
and a blank line is automatically set to 0 in the ram
also NO WHITESPACES AT THE START OR IN THE MIDDLE OF LINES IT WILL NOT WORK as of now
use ; for comments AFTER a line

IMPORTANT: always use a hashtag to halt the program, if no halt is specifed, the program will just give an error

e.g. (bad code)

03

01458

04

^ no hashtag at the end (baaad)

(good code)

03

01458

04 #

^ yayyy hashtag (good)

commands

01<address_here> = store current accumulator value at address specified. e.g. 0187 (stores accumulator value at address 87)
be careful not to overwrite any code you have stored whilst using this and any other commands that set an address to a value

02<address_here> = store specified address' value into the accumulator (overwriting what was previously in it) e.g. 0254 (stores address 54 value in accumulator)

03<_type><address_here> = if type = 1 then it is a string input and the value is stored from <address> and onwards, each character being encoded in ascii
if type = 0 then it is an integer input and stores value in accumulator

04 = outputs current value in accumulator

05<address_here> = adds the value in the accumulator and the value in the specified address, and overwrites the accumulator with the answer 
e.g. 0546 (adds accumulator value and value at address 46 and outputs the result to the accumulator)

06 = <address_here> = subtracts the value in the accumulator from the value in the specified address, and overwrites the accumulator with the answer 
e.g. 0646 (subtracts accumulator value from value at address 46 and outputs the result to the accumulator)

07<address_1(5 digits)><address_2> = branch if zero. moves the program counter to address_2 if address_1 is 0
e.g. 070013267 (if address 132's value is 0, the program counter will be set to excecute from address 67)

08<number> = an old thing i decided to keep (may be removed in the future) sets accumulator to number defined
e.g. 0871 (sets accumulator value to 71)

09 = converts value in accumulator to the corresponding ascii character and then outputs it (does not overwrite accumulator)
