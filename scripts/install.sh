#! /bin/bash

if [[ "$OSTYPE" == "win32"* ]]; then
        python -m pip install /r requirements.txt
else
        python3 -m pip3 install -r requirements.txt
fi

touch ../.env
