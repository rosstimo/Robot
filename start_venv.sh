#!/bin/bash

# Start the python virtual environment
echo "Starting python virtual environment"
echo "If this does not work, then you may need to install python3-venv"
# if ~/python/venv/bin/activate exists, then activate the virtual environment
# otherwise, create the virtual environment and activate it

if [ -f ~/python/venv/bin/activate ]; then
    source ~/python/venv/bin/activate
else
    python3 -m venv ~/python/venv
    source ~/python/venv/bin/activate
fi

# if requirements.txt exists, then install the requirements
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

# add ~/python/venv/bin to the beginning of PATH so that the python in the virtual environment is used

export PATH=~/python/venv/bin:$PATH

# if the virtual environment is activated, then the prompt will start with (venv)

echo "venv activated"
echo "run the command: 'deactivate' to exit the virtual environment"
