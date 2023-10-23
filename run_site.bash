#!/bin/sh

cd /volume1/Web/website
git pull

/usr/local/bin/python3 /volume1/Web/website/website.py &

while true; do

    # Calculate the elapsed time
    CURRENT_TIME=$(date +%s)
    ELAPSED_TIME=$((CURRENT_TIME - START_TIME))

    # Check if the time duration has exceeded
    if [ "$ELAPSED_TIME" -ge "$DURATION" ]; then
        git pull
        START_TIME=$(date +%s)
        echo pulled
    fi

    # Add a sleep interval if necessary
    sleep 5
done
