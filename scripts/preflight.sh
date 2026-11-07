#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")/.."
python scripts/validate.py
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/package.py
