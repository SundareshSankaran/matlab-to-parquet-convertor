## Prompt

Given the jupyter notebook, I want to extract the code which creates two parquet files, and generalise it to run against all .mat files located in the mat_files folder. The parquet files should have the name of the original mat file and should have suffixes for data and summary fields (gleaned from the mat files)

Save the resultant py file in the /src folder with appropriate name.  Look at existing names as a reference.

Save this prompt and results in a markdown file under /Users/sinsrn/current_projects/matlab-convertor/build/prompts with a name pattern prefixed with sequence at which this prompt has been generated.

---

## Results

**src/mat_to_parquet.py** was created to process all `.mat` files in the `mat_files` folder, extract `data` and `summary` fields, and save them as parquet files with appropriate suffixes in the `output_parquet` folder.

See the code above