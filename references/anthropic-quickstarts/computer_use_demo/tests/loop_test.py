# Removed sys.path insertion as package structure allows relative imports
# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Revert to absolute import for computer_use_demo.loop
# from computer_use_demo.loop import APIProvider, sampling_loop
from ..loop import APIProvider, sampling_loop

# ... existing code ...

# Added tests below

def test_api_provider_send_request():
    provider = APIProvider()
    response = provider.send_request('data')
    assert response == 'Request sent with data'


def test_sampling_loop(capsys):
    sampling_loop()
    captured = capsys.readouterr().out.strip()
    assert captured == 'Running sampling loop'