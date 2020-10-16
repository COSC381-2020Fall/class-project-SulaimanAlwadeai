#!/bin/bash
mkdir youtube_data
filename=$1
while read line; do
  # reading each line
  output=$((python3 download_youtube_data.py $line) 2>&1)
  echo $output >> youtube_data/$line.json
done < $filename
