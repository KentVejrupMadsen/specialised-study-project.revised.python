#!/usr/bin/env bash
bash .setup.sh

# setup of local environment
python -m venv .venv
source ./.venv/bin/activate

# Upgrades pip for the local environment
python -m pip install --upgrade pip

# installing required files
if [ -f requirements.txt ];
then
  pip install -r requirements.txt;
fi

# runs test environment
pytest
