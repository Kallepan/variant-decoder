#!/bin/bash

# This script is used to setup the environment for the project
# It will install all the required packages and libraries
# It will also create a virtual environment for the project

python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt # I should probably have a requirements.txt for dev and prod
