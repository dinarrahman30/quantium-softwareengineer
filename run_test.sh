#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the test suite
pytest test_dash.py

# Capture the exit code of pytest
exit_code=$?

# Return exit code 0 if all tests passed, otherwise return 1
if [ $exit_code -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed."
    exit 1
fi