#!/bin/bash

# Function to call
function="put_var_on_plevs"

# Only necessary if using put_var_on_p/zlevs functions
varname="z"

for init in "20Z"
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
