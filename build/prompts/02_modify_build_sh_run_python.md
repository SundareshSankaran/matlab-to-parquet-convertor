## Prompt

Given the instructions about a program detailed in the build/prompts folder, modify build.sh to insert a line to execute the Python program and deactivate the environment afterwards.  

Save the changes in the build.sh script. Save this prompt and results (annotating the prompt and results sections) as a markdown file (with a prefix number indicating the sequence of this prompt) in the /build/prompts folder.

---

## Results

**build/build.sh** was modified to add a line that runs the Python program after installing dependencies, and then deactivates the virtual environment:

```bash
# Run the Python program to convert .mat files to pandas dataframes
python ../src/mat_to_pandas.py ../mat_files

# Deactivate the virtual environment
deactivate
```

The Python program expects the .mat files to be in a folder named `mat_files` at the root of the workspace. Adjust the path as needed