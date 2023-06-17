#!/usr/bin/env bash
git submodule update --recursive

ls -a dataset/Reuters21578


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
bash ./.replicate.sh

#
export dataset_location_at="/tmp/dataset"

# runs test environment
pytest -s
