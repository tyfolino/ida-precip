#!/bin/bash

# Read in the WoFS forecast initialization time
init=$1
# Read in the variable you want to make
var=$2

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