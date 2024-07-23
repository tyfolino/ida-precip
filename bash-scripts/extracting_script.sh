#!/bin/bash

for init in "20Z" "21Z" "22Z" "23Z"
do
    for var in "U10" "V10"
    do
        bash /home/janoski/ida-scripts/bash-scripts/extract-var.sh $init $var
    done
done
