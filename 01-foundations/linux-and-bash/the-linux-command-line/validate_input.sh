#!/bin/bash

# read-validate: validate input

invalid_input () {
    echo "Invalid Input $REPLY" >&2
    exit 1
}

read -p "Enter a single item > "

[[ -z "$REPLY" ]] && invalid_input

(( "$(echo "$REPLY" | wc -w)" > 1 )) && invalid_input

if [[ "$REPLY" =~ ^[-[:alnum:]\._]+$ ]]; then
    echo "'$REPLY' is a valid filename."

    if [[ -e "$REPLY" ]]; then
        echo "And file '$REPLY' exists."
    else
        echo "However, file '$REPLY' does not exist."
    fi

    if [[ "$REPLY" =~ ^-?[[:digit:]]*\.[[:digit:]]+$ ]]; then
        echo "'$REPLY' is a floating point number."
    else
        echo "'$REPLY' is not a floating point number."
    fi

    if [[ "$REPLY" =~ ^-?[[:digit:]]$ ]]; then
        echo "'$REPLY' is an integer"
    else
        echo "'$REPLY' is not an integer."
    fi

else 
    echo "The string '$REPLY' is not a valid filenam"
fi
