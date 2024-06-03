#!/bin/bash

for init in "20Z"
do
    for var in "PB"
    do
        bash /home/janoski/ida-scripts/extract-var.sh $init $var
    done
done