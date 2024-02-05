#!/bin/bash

for VAR in {01..18}
do
wget -P /mnt/drive2/wof-runs "https://data.nssl.noaa.gov/thredds/fileServer/FRDD/WoFS/Forecast/2021/\
20210901/2000/ENS_MEM_${VAR}/wrfout_d01_2021-09-01_20:00:00"
done