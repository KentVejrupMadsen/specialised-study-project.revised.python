#!/usr/bin/env bash


cd ..
git submodule update --recursive


#
cp dataset/Reuters21578/dataset code/.data -R

#
cd code
python -m venv .venv
