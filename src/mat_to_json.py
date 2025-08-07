import os
import sys
import glob
import scipy.io
import numpy as np
import json

def mat_to_serializable(obj):
    """
    Recursively convert numpy types and arrays to Python native types for JSON serialization.
    Handles non-serializable types by converting them to strings.
    """
    if isinstance(obj, dict):
        return {k: mat_to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [mat_to_serializable(v) for v in obj]
    elif isinstance(obj, np.ndarray):
        # Recursively convert each element in the array
        return [mat_to_serializable(v) for v in obj.tolist()]
    elif isinstance(obj, (np.integer, np.floating, np.bool_)):
        return obj.item()
    elif isinstance(obj, bytes):
        try:
            return obj.decode(errors="replace")
        except Exception:
            return str(obj)
    elif isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj
    else:
        # For any other non-serializable type, convert to string
        return str(obj)

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
    convert_mat_to_json(mat_folder, output_folder)