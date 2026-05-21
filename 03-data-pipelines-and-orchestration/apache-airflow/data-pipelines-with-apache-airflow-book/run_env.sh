#!/bin/bash
set -e
VENV_DIR="venv"

echo "--- Starting Environment Setup ---"

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in ./$VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists. Skipping creation."
fi

echo "Installing/Updating dependencies..."
./"$VENV_DIR"/bin/pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    ./"$VENV_DIR"/bin/pip install -r requirements.txt
else
    echo "Warning: requirements.txt not found. Skipping installation."
fi

echo "--- Setup Complete! ---"
echo "To activate, run: source $VENV_DIR/bin/activate"
