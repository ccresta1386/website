#!/bin/bash

# Set the time duration in seconds
DURATION=295

git pull
python3 website.py&
pid=$!


# Get the start time
START_TIME=$(date +%s)

# Main loop
while true; do
    # Add your code here to run repeatedly

    # Calculate the elapsed time
    CURRENT_TIME=$(date +%s)
    ELAPSED_TIME=$((CURRENT_TIME - START_TIME))

    # Check if the time duration has exceeded
    if [ "$ELAPSED_TIME" -ge "$DURATION" ]; then
        echo "Script has run for 5 minutes. Exiting..."
        kill "$pid"
        exit
    fi

    # Add a sleep interval if necessary
    sleep 5
done