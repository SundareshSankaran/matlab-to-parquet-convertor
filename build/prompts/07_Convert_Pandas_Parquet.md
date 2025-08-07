## Prompt

How do I convert a pandas dataframe to a parquet file?

Save this prompt and results (annotating the prompt and results sections) as a markdown file (with a prefix number indicating the sequence of this prompt) in the /build/prompts folder.

---

## Result

You can convert a pandas DataFrame to a parquet file using the `to_parquet` method. You need to have either the `pyarrow` or `fastparquet` library installed.

**Example:**

```python
import pandas as pd

# Assuming df is your DataFrame
df.to_parquet('output_file.parquet', engine='pyarrow')
```

- Replace `'output_file.parquet'` with your desired file path.
- If you don't have `pyarrow` installed, you can install it with `pip install pyarrow`.

**Summary:**  
Use `df.to_parquet('filename.parquet', engine='pyarrow')` to save a DataFrame as a parquet