#!/bin/bash

# Function to call
function="put_var_on_zlevs"

# Only necessary if using put_var_on_p/zlevs functions
varname="V"

for init in "20Z" "21Z" "22Z" "23Z"
do
    # Set path using initialization time
    path="/mnt/drive2/wof-runs/$init"

    # Iterate through each file in the directory
    for file in $path/*
    do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            python ~/ida-scripts/utils/utils.py $function $filename $path --varname $varname
        fi
    done
done