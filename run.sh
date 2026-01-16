#!/bin/bash

cd "$(dirname "$0")"

# 1. Variables d'environnement pour stabiliser Qt sur Linux
# Désactive le sandbox Chromium qui cause souvent l'erreur QSocketNotifier
export QTWEBENGINE_DISABLE_SANDBOX=1
# Supprime les logs de debug inutiles dans la console
export QT_LOGGING_RULES="*.debug=false;qt.qwebenginecontext.debug=false"

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

if ! pip show PyQt5 > /dev/null 2>&1; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

echo "Démarrage de iFacturier Plus..."
python3 main.py