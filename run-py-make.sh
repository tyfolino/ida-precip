#!/bin/bash

# Read in the variable you want to make
var=$1

# Iterate through initializations
for init in "21Z" "22Z" "23Z" "00Z"
do

    # Specify the directory
    directory="/mnt/drive2/wof-runs/$init"

    # Check if the var subdirectory exists
    if [ ! -d "$directory/$var" ]; then
        # If it doesn't exist, create it
        mkdir "$directory/$var"
    else
        :
    fi

    # iterate through each file in the directory
    for file in $directory/*
    do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            python "/home/janoski/ida-scripts/make-$var.py" $filename $directory
        fi
    done
done