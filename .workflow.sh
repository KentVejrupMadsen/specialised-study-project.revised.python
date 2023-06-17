#!/usr/bin/env bash
# setup of local environment
python -m venv .venv
source ./.venv/bin/activate

#
export dataset_location_at='./dataset/Reuters21578/dataset'


# Upgrades pip for the local environment
python -m pip install --upgrade pip

# installing required files
if [ -f requirements.txt ];
then
  pip install -r requirements.txt;
fi

# Load required submodules
git submodule update --recursive

# runs test environment
pytest -s
