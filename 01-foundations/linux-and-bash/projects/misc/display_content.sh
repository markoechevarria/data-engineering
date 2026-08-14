#!/bin/bash

echo "Today is $(date)"
echo "Today is" $(date)

echo -e "\nEnter the path to directory"
read the_path

echo -e "\nThe path has the following files and folders: "
ls $the_path
