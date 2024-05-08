#!/bin/bash

for init in "20Z" "21Z" "22Z" "23Z"
do
    for var in "REL_VORT" "U" "V"
    do
        bash /home/janoski/ida-scripts/extract-var.sh $init $var
    done
done