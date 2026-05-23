# Bash Programming

## Bash

* Bash programming language can do very basic arithmetic
* Bash executes programs in order from the first line to the last line
* Anything written after a pound sign ( # ) is a comment and is not executed by Bash

### Math

* Simple arithmetic could be done with the `expr` command
* More complicated arithmetic could be performed by piping a string expression into `bc` using `echo`

### Variables

* Variables can be assigned with the equal sign (`=`) operator
* Strings or numbers can be assigned to variables
* The value of a variable can be accessed with the dolar sign (`$`) before the variable name

### User Input

* `read` stores a string that the user provides in a variable

### Logic and If/Else

* All bash program have an exit status. `true` has an exit status of 0 and `false` has an exit status of 1
* Conditional execution uses two operators: AND (`&&`) and OR (`||`) which you can use to control what command get executed based on their exit status
* Conditional expressions are always in double brackets ([[ ]]). They have an exit status of 0 if they contain a true assertion or 1 if they contain a false assertion.
* IF statements evaluate conditional expressions. If an expression is true then the code within an IF statement is executed, otherwise it is skipped.
* ELIF and ELSE statements also help control the flow of a Bash program, and IF statements can be nested within other IF statements.

### Arrays

* Arrays are a linear data structure with ordered elements which can be stored in variables.
* The each element of an array has an index and the first index is 0.
* Individual elements of an array can be accessed using their index.

### Braces

* Braces allow you create string sequences and expansions.
* To use variables with braces you need to use the eval command.

### Loops

* Loops allows you repeat sections of your program.
* FOR loops iterate through a sequence so that a variable that you assign takes on the value of every element of the sequence in every iteration of the loop.
* WHILE loops check a conditional statement at the beginning of every iteration. If the condition is equivalent to true then one iteration of the loop is executed and then the conditional statement is checked again. Otherwise the loop ends.
* IF statements and loops can be nested in order to make more powerful programming structures.v

### Functions

* Functions start with the function keyword followed by the name of the function and curly brackets ({}).
* Functions are small, reusable pieces of code that behave just like commands.
* You can use variables like $1, $2, and $@ in order to provide arguments to functions, just like a Bash script.
* Use the source command in order to read in a Bash script with function definitions so that you can use your functions in your shell.
* Use the local keyword to prevent your function from creating or modifying global variables.
* Be sure to echo the results of your function (if there are any) so that they can be captured with command substitution.v

### Writing programs

* Limiting a program to only doing one thing reduces the length of the program, and the shorter a program is the easier it is to fix if it contains bugs or if it needs to be revised.
* Writing short programs also helps the users of your code understand what’s going on in your code in the event that they need to read your code. Reading a poem induces a different cognitive load compared to reading a novel.
* Folks who don’t read the source code of your program (most users won’t - they shouldn’t have to) will be able to understand the inputs, outputs, and side effects of your program more easily.
* Using small programs to write a new program will increase the likelihood that the new program will also be small. Composability is the concept of stringing small programs together to create a new program.

* According to the Unix Philosophy you should keep your programs short, simple, and quiet.
* Use chmod to make your programs executable.
You can modify your ~/.bash_profile in order to make scripts and functions available to use on the command line.
* Use export to change an environmental variable.
















