#!/bin/bash
# Daemons is the module responsible for running the API
# and the Updater as daemons.


# Get the right paths
export WORK_DIR="$(dirname $0)"
cd "$WORK_DIR" || exit 1


# Configure Pyenv
export LOG='/tmp/amigo_investidor.log'
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi


# Installs the deps
cd ..
make install
pip install -U -r requirements_dev.txt
cd "$WORK_DIR"


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

