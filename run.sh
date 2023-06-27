#!/usr/bin/bash

source .venv/bin/activate

if [ $1=='dev' ]; then
  flask run --host=0.0.0.0 -p8000 --debugger --reload
else
  flask run --host=0.0.0.0 -p8000
fi
