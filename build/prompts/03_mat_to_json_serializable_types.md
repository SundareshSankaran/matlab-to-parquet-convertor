## Prompt

Given Python program to convert .mat to JSON, modify the program to also include code that checks the type of data attempted to be serialised and insert appropriate type conversion code for non-serialisable content.

Save the changes with the same name as earlier. Save this prompt and results (annotating the prompt and results sections) as a markdown file (with a prefix number indicating the sequence of this prompt) in the /build/prompts folder.

---

## Results

**src/mat_to_json.py** was updated to check the type of each object before serializing and to convert non-serializable types (such as bytes or unknown objects) to strings or appropriate Python types:

```python
def mat_to_serializable(obj):
    """
    Recursively convert numpy types and arrays to Python native types for JSON serialization.
    Handles non-serializable types by converting them to strings.
    """
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, (np.integer, np.floating, np.bool_)):
        return obj.item()
    elif isinstance(obj, dict):
        return {k: mat_to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [mat_to_serializable(v) for v in obj]
    elif isinstance(obj, bytes):
        return obj.decode(errors="replace")
    elif isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj
    else:
        # For any other non-serializable type, convert to string
        return str(obj)
```
This ensures that all data written to JSON is serializable, and unexpected types