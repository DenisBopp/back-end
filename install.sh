#!/usr/bin/bash
FOLDER=$1
set -x
mkdir ${FOLDER}
cd ${FOLDER}
python -m venv .venv
source .venv/bin/activate
cp ../requirements.txt ./
cp ../run.sh  ./
pip install -r requirements.txt