#!/bin/bash

# Get the current script directory
script_dir=$(dirname "$(realpath "$0")")

# Create the CSV file path
csv_file="$script_dir/filename.csv"

# Start an infinite loop
while true; do
    # Get total CPU usage (percentage)
    cpu=$(top -bn2 | grep '%Cpu' | tail -1 | awk '{print 100 - $8 "%"}')

    # Get total memory usage (percentage)
    mem=$(free | grep Mem | awk '{print $3/$2 * 100.0 "%"}')

    # Get the current date and time
    dat=$(date '+%Y-%m-%dT%H:%M:%S')

    # Log the data to the CSV file
    echo "$dat , $mem , $cpu"  >> "$csv_file"

    # Sleep for 300 seconds (5 minutes)
    sleep 300
done

echo "Script processed successfully."
