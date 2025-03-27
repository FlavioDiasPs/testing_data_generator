import json
import numpy as np
import random
import datetime

def generate_number(original, is_float=False):
    """
    Generate a number based on the original value using a normal distribution.
    Args:
        original: The original number (int or float).
        is_float: Boolean indicating if the output should be a float.
    Returns:
        A new number close to the original.
    """
    # Use the original value as the mean, with 10% as standard deviation
    mean = original
    std_dev = original * 0.1  # Adjust this based on desired variation
    if is_float:
        return round(np.random.normal(mean, std_dev), 2)
    else:
        return int(np.random.normal(mean, std_dev))

def generate_sample_data(example):
    """
    Generate sample data based on a JSON-like Python object.
    Args:
        example: A Python object (dict, list, int, float, etc.).
    Returns:
        A new object with realistic sample data.
    """
    # Handle dictionaries (JSON objects)
    if isinstance(example, dict):
        return {key: generate_sample_data(value) for key, value in example.items()}
    
    # Handle lists (JSON arrays)
    elif isinstance(example, list):
        return [generate_sample_data(item) for item in example]
    
    
    # Handle integers
    elif isinstance(example, int):
        return generate_number(example)
    
    # Handle floats
    elif isinstance(example, float):
        return generate_number(example, is_float=True)
    
    # Handle strings (basic handling; extend for dates if needed)
    elif isinstance(example, str):
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=len(example)))
    
    # Handle booleans
    elif isinstance(example, bool):
        return random.choice([True, False])
    
    # Handle null
    elif example is None:
        return None
    
    else:
        raise ValueError("Unsupported type in JSON structure")

# Example usage
if __name__ == "__main__":
    # Your sample JSON with the integer 300,000
    example_json = {
        "user_id": 300000,
        "name": "John",
        "scores": [300000, 310000],
        "details": {
            "age": 25,
            "salary": 50000.75
        }
    }
    
    # Generate sample data
    sample_data = generate_sample_data(example_json)
    
    # Print result
    print(json.dumps(sample_data, indent=2))