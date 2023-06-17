#!/usr/bin/env bash

python -m venv .venv
source ./.venv/bin/activate

export dataset_at=''
export location_to_application=''

# Load required submodules
git submodule update --recursive

pytest -s
