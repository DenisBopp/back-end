#!/usr/bin/bash

clear
DEV=$1
source .venv/bin/activate

set -x

if [ "$DEV" = "dev" ]; then
  echo "Running... Debug-Reload"
  flask run --host=0.0.0.0 -p8000 --debugger --reload
else
  echo "Running..."
  flask run --host=0.0.0.0 -p8000
fi
