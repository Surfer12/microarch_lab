# Adjust the sys.path so that references/anthropic-quickstarts is on PYTHONPATH
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Revert to absolute import for computer_use_demo.loop
from computer_use_demo.loop import APIProvider, sampling_loop

# ... existing code ...