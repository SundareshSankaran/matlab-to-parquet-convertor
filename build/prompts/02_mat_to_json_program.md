## Prompt

Given earlier prompt for a Python program to convert .mat to pandas, modify mat_to_pandas.py to a solution that converts a .mat file to a nested json, retaining only elements which are non-metadata keys, and saves the json file to an output folder within the project root folder.  

Save the changes as a new Python program. Save this prompt and results (annotating the prompt and results sections) as a markdown file (with a prefix number indicating the sequence of this prompt) in the /build/prompts folder.

---

## Results

**src/mat_to_json.py**:

```python
import os
import sys
import glob
import scipy.io
import numpy as np
import json

def mat_to_serializable(obj):
    """
    Recursively convert numpy types and arrays to Python native types for JSON serialization.
    """
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, (np.integer, np.floating, np.bool_)):
        return obj.item()
    elif isinstance(obj, dict):
        return {k: mat_to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [mat_to_serializable(v) for v in obj]
    else:
        return obj

def convert_mat_to_json(mat_folder, output_folder):
    """
    Converts all .mat files in mat_folder to nested JSON files in output_folder.
    Only non-metadata keys are retained.
    """
    os.makedirs(output_folder, exist_ok=True)
    mat_files = glob.glob(os.path.join(mat_folder, "*.mat"))
    for mat_file in mat_files:
        mat_data = scipy.io.loadmat(mat_file)
        # Remove MATLAB metadata keys
        mat_data = {k: v for k, v in mat_data.items() if not k.startswith('__')}
        # Convert to serializable format
        serializable_data = mat_to_serializable(mat_data)
        # Write to JSON file
        base_name = os.path.splitext(os.path.basename(mat_file))[0]
        json_path = os.path.join(output_folder, base_name + ".json")
        with open(json_path, "w") as f:
            json.dump(serializable_data, f, indent=2)
        print(f"Saved {json_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python mat_to_json.py <mat_folder> <output_folder>")
        sys.exit(1)
    mat_folder = sys.argv[1]
    output_folder = sys.argv[2]
    convert_mat_to_json(mat_folder,