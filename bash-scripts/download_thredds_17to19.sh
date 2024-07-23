#!/bin/bash

# Base target directory
BASE_TARGET_DIR="/mnt/drive2/new-wofs"

# Base URL for the THREDDS catalog page
BASE_CATALOG_URL="https://data.nssl.noaa.gov/thredds/catalog/FRDD/WoFS/Summary-Files/2021/WOFSRun20231106-164940d1"

# Times to loop through
TIMES=("17Z" "18Z" "19Z")
HOURS=("1700" "1800" "1900")
DATES=("20210901" "20210901" "20210901")

# Loop through each time and download the files
for i in ${!TIMES[@]}; do
    TARGET_DIR="$BASE_TARGET_DIR/${TIMES[$i]}"
    CATALOG_URL="$BASE_CATALOG_URL/${DATES[$i]}/${HOURS[$i]}/catalog.html"
    
    # Create the target directory if it doesn't exist
    mkdir -p "$TARGET_DIR"
    
    # Download the catalog HTML file
    wget -q -O catalog.html "$CATALOG_URL"
    
    # Extract file URLs from the HTML content
    FILE_URLS=$(grep -oP 'href="\K[^"]+' catalog.html | grep 'FRDD/WoFS/Summary-Files/2021/WOFSRun20231106-164940d1/.*/wofs.*.nc' | sed 's|catalog.html?dataset=|fileServer/|')
    
    # Download each file
    for FILE_URL in $FILE_URLS; do
        wget -P "$TARGET_DIR" "https://data.nssl.noaa.gov/thredds/$FILE_URL"
    done
    
    # Clean up
    rm catalog.html
    
    echo "Download for ${TIMES[$i]} completed!"
done

echo "All downloads completed!"
