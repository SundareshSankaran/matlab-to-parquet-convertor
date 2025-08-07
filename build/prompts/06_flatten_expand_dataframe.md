## Prompt

I've got a data frame with two columns, each row of which contain a nested numpy array of shape (1000, 1). How do I flatten this nested array and expand the number of rows in my dataframe?

Save this prompt and results (annotating the prompt and results sections) as a markdown file (with a prefix number indicating the sequence of this prompt) in the /build/prompts folder.

---

## Result

You can use `pd.DataFrame.explode` to expand each array into separate rows, but first you need to flatten the (1000, 1) arrays to 1D arrays. Here’s how you can do it:

```python
import numpy as np
import pandas as pd

# Example dataframe
# df = pd.DataFrame({'A': [np.random.rand(1000, 1) for _ in range(3)],
#                    'B': [np.random.rand(1000, 1) for _ in range(3)]})

# Step 1: Flatten each (1000, 1) array to (1000,)
for col in ['A', 'B']:
    df[col] = df[col].apply(lambda arr: arr.flatten())

# Step 2: Expand each column so each element becomes a row
df_expanded = df.apply(pd.Series.explode)

# Step 3: Reset index if needed
df_expanded = df_expanded.reset_index(drop=True)
```

Now, `df_expanded` will have 3 * 1000 rows (if you started with 3 rows), and each value in columns 'A' and 'B' will be a scalar.

**Summary:**  
- Flatten arrays with `.flatten()`
- Use `.explode()` to expand