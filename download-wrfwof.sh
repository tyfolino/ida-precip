#!/bin/bash

for ENS in {01..18}
do
# for DYHR in "01_20" "01_21" "01_22" "01_23" "02_00" "02_01"
for DYHR in "02_00" "02_01" "02_02" "02_03" "02_04" "02_05"
do
for MIN in {00..55..5}
do
wget -O "wrfwof_d01_2021-09-${DYHR}:${MIN}:00.${ENS}" \
"https://data.nssl.noaa.gov/thredds/fileServer/FRDD/WoFS/\
Forecast/2021/20210901/0000/ENS_MEM_${ENS}/wrfwof_d01_2021-09-${DYHR}:${MIN}:00"
done
done
wget -O "wrfwof_d01_2021-09-02_06:00:00.${ENS}" \
"https://data.nssl.noaa.gov/thredds/fileServer/FRDD/WoFS/\
Forecast/2021/20210901/0000/ENS_MEM_${ENS}/wrfwof_d01_2021-09-02_06:00:00"
done