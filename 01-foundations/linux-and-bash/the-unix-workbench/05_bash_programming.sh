#!/bin/bash

### Math

expr 5 + 2
expr 5 - 2
expr 5 \* 2
expr 5 / 2
expr 5 % 2

echo "22 / 7" | bc -l
echo "(6.5 / 0.5) + (6 * 2.2)" | bc -l

### Variables

chapter_number=5
echo $chapter_number

let chapter_number=$chapter_number+1
echo $chapter_number

the_empire_state="New York"
echo $the_empire_state

math_lines=$(cat README.md | wc -l)
echo $math_lines

echo "I went to the school in $the_empire_state"

echo "Script arguments: $@"
echo "First arg: $1. Second arg: $2."
echo "Number of arguments: $#"

### User Input

echo "Type in a string and then press Enter:"
read response
echo "You entered: $response"

### Logic and If/Else

echo $?
true
echo $?
false
echo $?

false && true && echo Hello
echo 1 && false && echo 3
echo Athos && echo Porthos && echo Aramis

[[ 4 -gt 3 ]]
echo $?

[[ -e math.sh ]] && echo t || echo f

number=7
[[ $number -gt 3 ]] && echo t || echo f
[[ $number -gt 10 ]] && echo t || echo f
[[ -e $number ]] && echo t || echo f

[[ rhythms =~ [aeiou] ]] && echo t || echo f
my_name=sean
[[ $my_name =~ ^s.+n$ ]] && echo t || echo f

[[ 7 -gt 2 ]] && echo t || echo f
[[ ! 7 -gt 2 ]] && echo t || echo f
[[ 6 -ne 3 ]] && echo t || echo f
[[ ! 6 -ne 3 ]] && echo t || echo

echo "Start program"

if [[ $1 -eq 4 ]]
then
  echo "$1 is my favorite number"
elif [[ $1 -gt 3 ]]
then
  echo "$1 is a great number"
else
  echo "You entered: $1, not what I was looking for."
fi

echo "End program"



if [[ $1 -gt 3 ]] && [[ $1 -lt 7 ]]
then
  echo "$1 is between 3 and 7"
elif [[ $1 =~ "Jeff" ]] || [[ $1 =~ "Roger" ]] || [[ $1 =~ "Brian" ]]
then
  echo "$1 works in the Data Science Lab"
else
  echo "You entered: $1, not what I was looking for."
fi

### Arrays

plagues=(blood frogs lice flies sickness boils hail locusts darkness death)
echo ${plagues[0]}
echo ${plagues[3]}
echo ${plagues[*]}

plagues[4]=disease
echo ${plagues[*]}
echo ${plagues[*]:5:3}
echo ${#plagues[*]}

dwarfs=(grumpy sleepy sneezy doc)
echo ${dwarfs[*]}
dwarfs+=(aea aea aeaaea)
echo ${dwarfs[*]}

### Braces

echo {0..9}
echo {a..e}
echo a{0..4}c
echo {1..3}{A..C}
echo {{1..3},{a..c}}

### Loops

echo "Before Loop"

for i in {1..3}
do
    echo "i is equal to $i"
done

echo "After Loop"


count=3
while [[ $count -gt 0 ]]
do
  echo "count is equal to $count"
  let count=$count-1
done












