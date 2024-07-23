#!/bin/bash

# Define the target directory
TARGET_DIR="/mnt/drive2/new-wofs/20Z"

# Create the target directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Base URL for the THREDDS catalog page
CATALOG_URL="https://data.nssl.noaa.gov/thredds/catalog/FRDD/WoFS/Summary-Files/2021/WOFSRun20231106-164940d1/20210901/2000/catalog.html"

# Download the catalog HTML file
wget -q -O catalog.html "$CATALOG_URL"

# Extract file URLs from the HTML content
FILE_URLS=$(grep -oP 'href="\K[^"]+' catalog.html | grep 'FRDD/WoFS/Summary-Files/2021/WOFSRun20231106-164940d1/20210901/2000/wofs.*.nc' | sed 's|catalog.html?dataset=|fileServer/|')

# Download each file
for FILE_URL in $FILE_URLS; do
    wget -P "$TARGET_DIR" "https://data.nssl.noaa.gov/thredds/$FILE_URL"
done

# Clean up
rm catalog.html

echo "Download completed!"
