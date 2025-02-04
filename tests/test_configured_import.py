#!/usr/bin/env python3
import sys
import os

# Dynamically add the project root to sys.path to ensure internal modules can be imported
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print(f"Added project root to sys.path: {project_root}")
else:
    print(f"Project root already in sys.path: {project_root}")

# Attempt to import a module from computer_use_demo
try:
    # Adjust the import based on your internal structure (replace 'loop' with an actual module if needed)
    from computer_use_demo import loop
    print("Successfully imported computer_use_demo.loop!")
except ImportError as e:
    print("Failed to import computer_use_demo:", e)

if __name__ == '__main__':
    print("Test module execution complete.")