#!/bin/bash

for init in "21Z" "22Z" "23Z" "00Z"
do
    for var in "HGT" "T2" "PSFC"
    do
        bash /home/janoski/ida-scripts/extract-var.sh $init $var
    done
done