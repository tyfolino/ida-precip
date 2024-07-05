#!/bin/bash

# Get user input
# echo "Input initialization time in the form ##Z"
# read init
# echo "Input variable name."
# read var
init=$1
var=$2

# Specify the directory
directory="/mnt/drive2/wof-runs/$init"

# Make a new directory
mkdir "$directory/$var"

# iterate through each file in the directory
for file in $directory/*
do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        # echo "$directory/$var/$filename"
        ncks -v $var $file "$directory/$var/$filename"
    fi
done