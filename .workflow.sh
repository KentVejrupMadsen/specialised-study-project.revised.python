#!/usr/bin/env bash
ls -a

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

# Load required submodules
git submodule update --recursive
bash ./.replicate.sh

#
export dataset_location_at="/tmp/dataset"

# runs test environment
pytest -s
