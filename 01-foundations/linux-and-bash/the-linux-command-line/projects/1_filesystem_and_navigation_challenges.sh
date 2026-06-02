#!/bin/bash

## Create structure

path="$(pwd)/data-lake"

create_structure () {

    if [ -d "$path" ]; then

        echo "data-lake directory already exists"

    else 

        echo "Creating data-lake directory"
        mkdir -p "$path"/{staging,processed,archive,scripts,raw/{sales,users,logs}}

    fi

}

delete_structure () {

    echo "Deleting data-lake directory"

    rm -rI "$path"
}

create_csvs () {

    echo "Creating csvs in /raw/sales"

    for i in {1..100}; do

        date=$(date +%d-%m-%y-%H-%M-%S-%3N)
        touch "$path/raw/sales/$date.csv"

    done
}

compress_files () {

    echo "Compressing files in /raw/sales"

    tar -czvf sales_compressed.tar.gz "$path/raw/sales"

}

main () {

    option=""

    while [[ $option != "5" ]]
    do

        echo """
File Systema dnd Navigation Challenges:

1) Create structure
2) Delete structure
3) Create csv
4) Compress files
5) Exit
        """
        read -p "Select an option: " option

        case "$option" in
        
            1) create_structure ;;
            2) delete_structure ;;
            3)create_csvs ;;
            4) compress_files ;;
            5) option="5";;
            *) optionn=""

        esac

    done

}

main
