#!/bin/bash

for ENS in {01..18}
do
for DYHR in "01_23" "02_00" "02_01" "02_02" "02_03" "02_04" "02_05"
do
for MIN in {00..55..5}
do
if [ "$DYHR" = "01_23" ] && [[ "$MIN" = "00" || "$MIN" = "05" || "$MIN" = "10" ||
"$MIN" = "15" || "$MIN" = "20" || "$MIN" = "25" ]]; then
:
elif [ "$DYHR" = "02_23" ] && [[ "$MIN" = "00" || "$MIN" = "05" || "$MIN" = "10" ||
"$MIN" = "15" || "$MIN" = "20" || "$MIN" = "25" ]]; then
:
else
:
fi
done
done

done