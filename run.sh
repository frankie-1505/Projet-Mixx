#!/bin/bash

cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

if ! pip show PyQt5 > /dev/null 2>&1; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

python3 main.py
