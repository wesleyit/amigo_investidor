#!/bin/bash
# Daemons is the module responsible for running the API
# and the Updater as daemons.

export WORK_DIR="$(dirname $0)"
cd "$WORK_DIR" || exit 1
export LOG='/tmp/amigo_investidor.log'

# Start the Updater
python updater.py &> "$LOG" &
disown

# Start the Flask API
python api.py &> "$LOG" &
disown

# Keep the process running (required by Docker)
echo "Following the log. Hit <CTRL+C> to exit..."
sleep 2
tail -f "$LOG"
