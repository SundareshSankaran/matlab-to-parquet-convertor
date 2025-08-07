import os
import sys
import glob
import scipy.io
import pandas as pd

def load_mat_files_to_dataframes(mat_folder):
    """
    Loads all .mat files in the given folder and converts them to pandas DataFrames.
    Returns a dictionary mapping filenames to DataFrames.
    """
    mat_files = glob.glob(os.path.join(mat_folder, "*.mat"))
    dataframes = {}
    for mat_file in mat_files:
        mat_data = scipy.io.loadmat(mat_file)
        # Remove MATLAB metadata keys
        mat_data = {k: v for k, v in mat_data.items() if not k.startswith('__')}
        # Convert each variable in the .mat file to a DataFrame if possible
        for var_name, value in mat_data.items():
            print(type(value))
            try:
                df = pd.DataFrame(value)
                print(df.head(10))
                dataframes[f"{os.path.basename(mat_file)}::{var_name}"] = df
            except Exception as e:
                print(f"Error converting variable '{var_name}' in file '{mat_file}': {e}")
                # If conversion fails, skip this variable
                continue
    return dataframes

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mat_to_pandas.py <mat_folder>")
        sys.exit(1)
    mat_folder = sys.argv[1]
    dfs = load_mat_files_to_dataframes(mat_folder)
    print(f"Loaded {len(dfs)} dataframes from .mat files in '{mat_folder}'.")
    # DataFrames are available in the 'dfs' dictionary in memory