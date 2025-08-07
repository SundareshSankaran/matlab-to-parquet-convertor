## Prompt

Create a Python program for the following purpose: Given a number of .mat files representing Matlab data files, when the user runs a Python program to convert these files into pandas dataframes, a conversion happens which results in output pandas data frames available in memory.  

Save the result Python program in a src folder at the root directory of this workspace. Save this prompt and results (annotating the prompt and results sections) as a markdown file (with a prefix number indicating the sequence of this prompt) in the /build/prompts folder.

---

## Results

**src/mat_to_pandas.py**:

```python
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
            try:
                df = pd.DataFrame(value)
                dataframes[f"{os.path.basename(mat_file)}::{var_name}"] = df
            except Exception:
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
    # DataFrames are available in the 'dfs' dictionary