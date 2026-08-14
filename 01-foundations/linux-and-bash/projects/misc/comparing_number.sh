#!/bin/bash

i=1

while [[ $i < 5 ]]; do

	echo "$i. Enter a number: "
	read number

	if [ $number -gt 0 -a $number -lt 90 ]; then
	
		echo "$number is greater than 0 and less than 90"

	elif [ $number -lt 0 ]; then

		echo "$number is less than 0"

	else

		echo "$number is greater than 90"

	fi

	(( i += 1 ))

done
