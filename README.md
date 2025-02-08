HOW TO USE:

at the start of your code file use a ! and a number to define the time it takes in seconds to do part of a cycle (this is not necassary and is automatically set to 1)

also just so you know if you have used the ! at the start, the ram address you are storing your instruction in is line number - 2, if not it is line number - 1
and a blank line is automatically set to 0 in the ram
also NO WHITESPACES AT THE END, START OR IN THE MIDDLE OF LINES IT WILL NOT WORK as of now

IMPORTANT: always use a hashtag to halt the program, if no halt is specifed, the program will just give an error

e.g. (bad code)

3
1458
4

^ no hashtag at the end (baaad)

(good code)

3
1458
4
#
^ yayyy hashtag (good)

commands

1<address_here> = store current accumulator value at address specified. e.g. 187 (stores accumulator value at address 87)
be careful not to overwrite any code you have stored whilst using this and any other commands that set an address to a value

2<address_here> = store specified address' value into the accumulator (overwriting what was previously in it) e.g. 254 (stores address 54 value in accumulator)

3 = take a user input and store it in the accumulator

4 = outputs current value in accumulator

5<address_here> = adds the value in the accumulator and the value in the specified address, and overwrites the accumulator with the answer 
e.g. 546 (adds accumulator value and value at address 46 and outputs the result to the accumulator)

6<address_here> = subtracts the value in the accumulator and the value in the specified address, and overwrites the accumulator with the answer 
e.g. 692 (subtracts value at address 92 from value in accumulator and outputs to the accumulator)

7<address_1(3 digits)><address_2> = branch if zero. moves the program counter to address_2 if address_1 is 0
e.g. 713267 (if address 132's value is 0, the program counter will be set to excecute from address 67)

8<number> = an old thing i decided to keep (may be removed in the future) sets accumulator to number defined
e.g. 871 (sets accumulator value to 71)

9 = converts value in accumulator to the corresponding ascii character and then outputs it (does not overwrite accumulator)
