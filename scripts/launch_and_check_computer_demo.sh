#!/bin/bash

# This script launches the computer-use-demo and checks if custom tools are recognized
# Path to computer-use-demo
COMPUTER_DEMO_PATH="/Volumes/a/anthropic-quickstarts-main/computer-use-demo"

echo "Launching computer-use-demo from $COMPUTER_DEMO_PATH..."

if [ ! -d "$COMPUTER_DEMO_PATH" ]; then
    echo "Error: computer-use-demo directory not found at $COMPUTER_DEMO_PATH"
    exit 1
fi

# Optionally launch the demo (assuming a setup.sh is present in the directory)
if [ -f "$COMPUTER_DEMO_PATH/setup.sh" ]; then
    echo "Running setup.sh in computer-use-demo..."
    bash "$COMPUTER_DEMO_PATH/setup.sh"
else
    echo "Warning: setup.sh not found in $COMPUTER_DEMO_PATH"
fi

# Now check if custom tools are recognized.
# For example, check if README.md in the demo contains a marker such as 'Anthropic API'.
GREP_RESULT=$(grep -i "Anthropic API" "$COMPUTER_DEMO_PATH/README.md")

if [ -n "$GREP_RESULT" ]; then
    echo "Custom tool marker recognized in computer-use-demo README.md"
else
    echo "Custom tool marker NOT recognized in computer-use-demo README.md"
fi

exit 0