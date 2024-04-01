#!/bin/bash

# Function to call
function="make_mslp"

for init in "20Z" "01Z"
do
    # Set path using initialization time
    path="/mnt/drive2/wof-runs/$init"

    # Iterate through each file in the directory
    for file in $path/*
    do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            python ~/ida-scripts/utils/utils.py $function $filename $path
        fi
    done
done