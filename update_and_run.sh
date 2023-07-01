#!/bin/sh
pip3 install Flask
pip3 install Flask-Limiter
# Set the time duration in seconds
DURATION=295

cd /volume1/Web/website
git pull

/usr/local/bin/python3 /volume1/Web/website/website.py >> /tmp/site_1.log 2>&1 &
pid=$!

# Get the start time
START_TIME=$(date +%s)

# Main loop
while true; do

    # Calculate the elapsed time
    CURRENT_TIME=$(date +%s)
    ELAPSED_TIME=$((CURRENT_TIME - START_TIME))

    # Check if the time duration has exceeded
    if [ "$ELAPSED_TIME" -ge "$DURATION" ]; then
        git pull
        START_TIME=$(date +%s)
    fi

    # Add a sleep interval if necessary
    sleep 5
done
