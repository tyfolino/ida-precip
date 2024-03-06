#!/bin/bash

for init in "20Z" "01Z"
do
    for var in "HGT" "T2" "PSFC"
    do
        bash /home/janoski/ida-scripts/extract-var.sh $init $var
    done
done