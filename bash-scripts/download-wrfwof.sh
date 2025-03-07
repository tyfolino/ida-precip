#!/bin/bash

for ENS in {01..18}
do
for DYHR in "02_01" "02_02" "02_03" "02_04" "02_05" "02_06"
do
for MIN in {00..55..5}
do
wget -O "wrfwof_d01_2021-09-${DYHR}:${MIN}:00.${ENS}" \
"https://data.nssl.noaa.gov/thredds/fileServer/FRDD/WoFS/\
Forecast/2021/20210901/0100/ENS_MEM_${ENS}/wrfwof_d01_2021-09-${DYHR}:${MIN}:00"
done
done
wget -O "wrfwof_d01_2021-09-02_07:00:00.${ENS}" \
"https://data.nssl.noaa.gov/thredds/fileServer/FRDD/WoFS/\
Forecast/2021/20210901/0100/ENS_MEM_${ENS}/wrfwof_d01_2021-09-02_07:00:00"
done