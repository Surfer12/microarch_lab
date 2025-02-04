# Added to ensure the parent directory is in PYTHONPATH
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# ... existing code ...

# Changed the import to a relative import
from ..loop import APIProvider, sampling_loop