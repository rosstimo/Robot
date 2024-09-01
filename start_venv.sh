#!/bin/bash

# Start the python virtual environment
python3 -m venv ~/python/venv &&
source ~/python/venv/bin/activate &&

# if requirements.txt exists, then install the requirements
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

# add ~/python/venv/bin to the beginning of PATH so that the python in the virtual environment is used
export PATH=~/python/venv/bin:$PATH

# if the virtual environment is activated, then the prompt will start with (venv)
echo "run: 'deactivate' to exit the virtual environment"
