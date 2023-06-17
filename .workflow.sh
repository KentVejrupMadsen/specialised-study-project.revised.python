#!/usr/bin/env bash

python -m venv .venv
source ./.venv/bin/activate



export dataset_at=''
export location_to_application=''

pytest -s
