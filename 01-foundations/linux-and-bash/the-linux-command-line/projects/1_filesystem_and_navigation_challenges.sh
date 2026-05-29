#!/bin/bash

## Create structure

create_structure () {

    if [ -d "data-lake" ]; then

        echo "data-lake directory already exists"

    else 

        echo "Creating data-lake directory"
        mkdir -p data-lake/{staging,processed,archive,scripts,raw/{sales,users,logs}}

    fi

}

create_csvs () {

    for i in {1..100}; do

        date = date
        echo "$i"
    done
}

create_csvs


