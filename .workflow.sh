#!/usr/bin/env bash

python -m venv .venv
source ./.venv/bin/activate

export dataset_at=''
export location_to_application=''

python -m pip install --upgrade pip
pip install pytest

if [ -f requirements.txt ];
then
  pip install -r requirements.txt;
fi

# Load required submodules
git submodule update --recursive

pytest -s
