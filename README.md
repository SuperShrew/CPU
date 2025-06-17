NOTICE: this has been discontinued and restarted in a different repository. if you want to use this then use the latest one on the beta branch















HOW TO USE:

at the start of your code file use a ! and a number to define the time it takes in seconds to do part of a cycle (this is not necassary and is automatically set to 1)

also just so you know if you have used the ! at the start, the ram address you are storing your instruction in is line number - 2, if not it is line number - 1
and a blank line is automatically set to 0 in the ram
also NO WHITESPACES AT THE START OR IN THE MIDDLE OF LINES IT WILL NOT WORK as of now
use ; for comments AFTER a line

IMPORTANT: always use a hashtag to halt the program, if no halt is specifed, the program will just give an error

e.g. (bad code)



^ no hashtag at the end (baaad)

(good code)



^ yayyy hashtag (good)

commands

01<address_here> = store current accumulator value at address specified. e.g. 0187 (stores accumulator value at address 87)
be careful not to overwrite any code you have stored whilst using this and any other commands that set an address to a value

02<address_here> = store specified address' value into the accumulator (overwriting what was previously in it) e.g. 0254 (stores address 54 value in accumulator)



04 = outputs current value in accumulator



08<number> = an old thing i decided to keep (may be removed in the future) sets accumulator to number defined
e.g. 0871 (sets accumulator value to 71)


