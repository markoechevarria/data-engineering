# 27. Flow control: Branching with if

## if Statements

```
if commands; then
    commands
[elif commands; then
    commands...]
[else
    commands]
fi
```

```
x=5
if [ "$x" -eq 5 ]; then
    echo "x equals 5."
else
    echo "x does not equal 5."
fi
```
## Exit Status

* Commands (including the scripts and shell functions we write) issue a value to the system when they terminate, called an exit status. By convention, a value of zero indicates success and any other value indicates failure

```
echo $?
if true; then echo "It's true.; fi
```
* `test expression`: expression is evaluated as either true or false

## File expressions

```
#!/bin/bash
# test-file: Evaluate the status of a file

FILE=~/.bashrc
if [ -e "$FILE" ]; then
    if [ -f "$FILE" ]; then
        echo "$FILE is a regular file."
    fi
    if [ -d "$FILE" ]; then
        echo "$FILE is a directory."
    fi
    if [ -r "$FILE" ]; then
        echo "$FILE is readable."
    fi
    if [ -w "$FILE" ]; then
        echo "$FILE is writable."
    fi
    if [ -x "$FILE" ]; then
        echo "$FILE is executable/searchable."
    fi
else
    echo "$FILE does not exist"
    exit 1
fi
exit
```
## String expressions

* string: string is not null.
* -n string: The length of string is greater than zero.
* -z string: The length of string is zero.
* string1 = string2: string1 and string2 are equal. Single or double equal signs
* string1 == string2: may be used. The use of double equal signs is greatly preferred, but it is not POSIX compliant.
* string1 != string2: string1 and string2 are not equal.
* string1 > string2: string1 sorts after string2.
* string1 < string2: string1 sorts before string2.

## Integer expressions

* integer1 -eq integer2: integer1 is equal to integer2.
* integer1 -ne integer2: integer1 is not equal to integer2.
* integer1 -le integer2: integer1 is less than or equal to integer2.
* integer1 -lt integer2: integer1 is less than integer2.
* integer1 -ge integer2: integer1 is greater than or equal to integer2.
* integer1 -gt integer2: integer1 is greater than integer2.

## Modern Version of test

`string1 =~ regex`

```
if [[ "$INT" =~ ^-?[0-9]+$ ]]; then
    if [ "$INT" -eq 0 ]; then
        echo "INT is zero."
    else
        if [ "$INT" -lt 0 ]; then
            echo "INT is negative."
        else
            echo "INT is positive."
        fi
        if [ $((INT % 2)) -eq 0 ]; then
            echo "INT is even."
        else
            echo "INT is odd."
        fi
    fi
else
    echo "INT is not an integer." >&2
    exit 1
fi
```

## (( ))—Designed for Integers

* In addition to the [[ ]] compound command, bash also provides the (( )) compound command, which is useful for operating on integers.

`if ((1)); then echo "It is true."; fi`

```
INT=-5
if [[ "$INT" =~ ^-?[0-9]+$ ]]; then
    if ((INT == 0)); then
        echo "INT is zero."
    else
        if ((INT < 0)); then
            echo "INT is negative."
        else
            echo "INT is positive."
        fi
        if (( ((INT % 2)) == 0)); then
            echo "INT is even."
        else
            echo "INT is odd."
        fi
    fi
else
    echo "INT is not an integer." >&2
    exit 1
fi
```

## Combining Expressions

* AND | -a | &&
* OR  | -o | ||
* NOT | !  |  !

## Control Operators: Another Way to Branch

* command1 && command2
* command1 || command2



