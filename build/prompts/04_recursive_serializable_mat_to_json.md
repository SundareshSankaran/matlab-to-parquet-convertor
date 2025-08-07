## Prompt

Given Python program to convert .mat to JSON, modify the serializable part of the function to recursively, and not just once, check the type of data attempted to be serialised and insert appropriate type conversion code for non-serialisable content.

Save the changes with the same name as earlier . Save this prompt and results (annotating the prompt and results sections) as a markdown file (with a prefix number indicating the sequence of this prompt) in the /build/prompts folder.

---

## Results

**src/mat_to_json.py** was updated so that the `mat_to_serializable` function now recursively checks and converts all nested data structures, including arrays, lists, tuples, and dictionaries, to ensure all content is serializable for JSON output:

```python
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
```
This ensures all nested and complex data structures are handled