#!/bin/bash

for ENS in {01..18}
do
for DYHR in 01_20 02_02
do
wget -O "wrfout_d01_2021-09-${DYHR}:00:00.${ENS}" \
"https://data.nssl.noaa.gov/thredds/fileServer/FRDD/WoFS/\
Forecast/2021/20210901/2000/ENS_MEM_${ENS}/wrfout_d01_2021-09-${DYHR}:00:00"
done
done