## Prompt

Modify given program to ensure that for every new run of this program, any parquet files already existing in the output_parquet folder are moved to a subfolder called done.

Save the modified py file in the /src folder with same name.

Save this prompt and results in a markdown file under /Users/sinsrn/current_projects/matlab-convertor/build/prompts with a name pattern prefixed with sequence at which this prompt has been generated.

---

## Results

The program was updated so that at the start of each run, any existing `.parquet` files in the `output_parquet` folder are moved to a `done` subfolder within `output_parquet`. This ensures that only newly generated parquet files remain in the main output folder after each run.

See the updated code