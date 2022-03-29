#!/bin/bash
VIRTENV = venv
if [ -d "$VIRTENV" ]; then
source ./venv/bin/activate
pip install pandas
else
python3 -m venv venv
source ./venv/bin/activate
pip install pandas
pip install --upgrade pip
pip install -r requirements.txt
fi
python3 -Wignore main.py