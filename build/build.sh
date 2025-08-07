#!/usr/bin/env bash
set -e
trap 'echo "Error occurred at line $LINENO. Exiting."; exit 1' ERR

# Check for required files
if [ ! -f requirements.txt ]; then
  echo "Error: requirements.txt not found."
  exit 1
fi

# Create Python virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install uv (fast Python package installer)
pip install uv

# Install dependencies from requirements.txt using uv
uv pip install -r requirements.txt

# Run the Python program to convert .mat files to parquet
python ../src/mat_to_parquet.py ../mat_files ../output_parquet

# Deactivate the virtual environment
deactivate