# 34. Strings and numbers

## Parameter expansion

* $a : the simplest form of parameter expansion is reflected in the ordinary use of variables
* ${a}: simple parameters may also be surrounded by braces

## Expansion to manage empty variables

* `${parameter:-word}`: if parameter is unset or is empty, this expansion results in the value of word. If parameter is not empty, the expansion resultsin the value of parameter
* `${parameter:=word}`: if parameter is unset or is empty, this expansion results in the valur of word. In addition the value of word is assigned to parameter. If parameter is not empty, the expansion results in the value of parameter
* `{parameter:?word}`: if parameter is unset or empty, this expansion causes the script to exit with an error, and the contents of word are sent to standard error. If parameter is not empty, the expansion results in the value of parameter
* `{parameter:+word}`: If parameter is unset or empty, the expansion results in nothing. If parameter is not empty, the value of word is substituted for parameter ; however, the value of parameter is not changed.

## Arithmetica Evaluation and Expansion

* `$((expression))`: expression is a valid arithmetic expression

## Bit operations

* \~: bitwise negation, negate all the bits in a number
* \<\<: left bitwise shift, shift all the bits in a number to the left
* \>\>: right bitwise shift, shift all the bits in a number to the right
* \&: bitwise and, perform an and operation on all the bits in two numbers
* \|: bitwise or, perform an or operation on all the bits in two number
* \^: bitwise xor, perform an exclusive or operation on all the bits in two number

## Logic

* \<\=: Less than or equal to.
* \>\=: Greater than or equal to.
* \<: Less than.
* \>: Greater than.
* \=\=: Equal to.
* \!\=: Not equal to.
* \&\&: Logical AND.
* \|\|: Logical OR.
* expr1?expr2:expr3: Comparison (ternary) operator. If expression expr1 evaluates to be nonzero (arithmetic true), then expr2; else expr3.

