# Your Assignment Parameters

These are your unique values for Lab 3. Use these exact values in your code.

## Task Values

| Parameter | Your Value |
|-----------|------------|
| Sample Count | {sample_count} samples |
| Rock Types | {rock_types} |
| Grade Range | {grade_range} |

## Task 1: List Operations (20 marks)

Create `src/lab3_lists.py` demonstrating list creation, indexing, and methods.

**Requirements:**
- Create a list of {sample_count} sample depths (integers between 100 and 500)
- Create a list of rock types from your assigned types: {rock_types}
- Demonstrate positive and negative indexing
- Use at least 3 list methods (append, extend, sort, etc.)

```python
# lab3_lists.py
# Your Name: [YOUR NAME]
# Student ID: [YOUR ID]

# TODO: Create a list of sample depths
# Use {sample_count} depths between 100 and 500 meters
depths = []  # Replace with your list

# TODO: Create a list of rock types from your assigned types
rock_types = []  # Replace with your assigned rock types: {rock_types}

# TODO: Demonstrate indexing
# Print the first depth (index 0)
# Print the last depth (negative index)
# Print a slice of depths (e.g., indices 2-5)

# TODO: Use list methods
# - Append a new depth
# - Sort the depths
# - Find the maximum depth using max()

# TODO: Print results
```

## Task 2: Dictionary Operations (20 marks)

Create `src/lab3_dictionaries.py` demonstrating dictionary creation and access.

**Requirements:**
- Create a sample record dictionary with keys: sample_id, rock_type, grade, depth
- Use grades within your assigned range: {grade_range}
- Demonstrate dictionary methods (keys, values, items, get)
- Create a nested dictionary for multiple samples

```python
# lab3_dictionaries.py
# Your Name: [YOUR NAME]
# Student ID: [YOUR ID]

# TODO: Create a sample record dictionary
sample = {
    'sample_id': 'GEO-001',
    'rock_type': '',  # Use one of your rock types
    'grade': 0.0,     # Use a grade within {grade_range}
    'depth': 0        # Use a depth value
}

# TODO: Access dictionary values
# Print each value using its key

# TODO: Use dictionary methods
# - Get all keys
# - Get all values
# - Get all key-value pairs
# - Use get() with a default value

# TODO: Create a nested dictionary with multiple samples
samples_db = {
    'GEO-001': {...},
    'GEO-002': {...},
    # Add more samples
}
```

## Task 3: Sample Collection Manager (25 marks)

Create `src/lab3_sample_manager.py` with functions to manage a collection of samples.

**Requirements:**
- Function to add a sample to a collection (list of dictionaries)
- Function to find samples by rock type
- Function to update a sample's grade
- Function to remove a sample by ID
- Use your assigned rock types: {rock_types}

```python
# lab3_sample_manager.py
# Your Name: [YOUR NAME]
# Student ID: [YOUR ID]

def create_sample_collection():
    """Create and return an empty sample collection (list)."""
    # TODO: Return an empty list
    pass

def add_sample(collection, sample_id, rock_type, grade, depth):
    """Add a new sample to the collection."""
    # TODO: Create a sample dictionary and append to collection
    # Return the updated collection
    pass

def find_by_rock_type(collection, rock_type):
    """Find all samples matching the given rock type."""
    # TODO: Return a list of matching samples
    pass

def update_grade(collection, sample_id, new_grade):
    """Update the grade of a sample by its ID."""
    # TODO: Find sample by ID and update its grade
    # Return True if found and updated, False otherwise
    pass

def remove_sample(collection, sample_id):
    """Remove a sample from the collection by ID."""
    # TODO: Remove the sample if found
    # Return True if removed, False if not found
    pass

# Main code to demonstrate functions
if __name__ == "__main__":
    # Create collection and add samples using your rock types
    collection = create_sample_collection()

    # TODO: Add at least {sample_count} samples
    # TODO: Demonstrate each function
```

## Task 4: Computing Statistics (20 marks)

Create `src/lab3_statistics.py` with functions to compute statistics from lists.

**Requirements:**
- Function to calculate average grade
- Function to find min and max depths
- Function to count samples by rock type
- Use list comprehensions where appropriate

```python
# lab3_statistics.py
# Your Name: [YOUR NAME]
# Student ID: [YOUR ID]

def calculate_average_grade(samples):
    """Calculate the average grade from a list of sample dictionaries."""
    # TODO: Use list comprehension to extract grades
    # TODO: Calculate and return average
    pass

def find_depth_range(samples):
    """Find the minimum and maximum depths."""
    # TODO: Return a tuple (min_depth, max_depth)
    pass

def count_by_rock_type(samples):
    """Count samples for each rock type."""
    # TODO: Return a dictionary with rock_type: count
    pass

def get_high_grade_samples(samples, threshold):
    """Return samples with grade above threshold."""
    # TODO: Use list comprehension with condition
    pass

# Main code
if __name__ == "__main__":
    # Create sample data using your assigned values
    samples = [
        {'sample_id': 'GEO-001', 'rock_type': '', 'grade': 0.0, 'depth': 0},
        # Add more samples from your assigned rock types: {rock_types}
    ]

    # TODO: Test each function and print results
```

## Task 5: Filtering and Sorting (15 marks)

Create `src/lab3_filters.py` with functions for filtering and sorting samples.

**Requirements:**
- Function to filter samples by depth range
- Function to sort samples by grade (ascending/descending)
- Function to get top N samples by grade
- Use your grade range: {grade_range}

```python
# lab3_filters.py
# Your Name: [YOUR NAME]
# Student ID: [YOUR ID]

def filter_by_depth_range(samples, min_depth, max_depth):
    """Filter samples within the given depth range."""
    # TODO: Return samples where min_depth <= depth <= max_depth
    pass

def sort_by_grade(samples, descending=False):
    """Sort samples by grade."""
    # TODO: Return a new sorted list (don't modify original)
    # Use sorted() with key parameter
    pass

def get_top_n_by_grade(samples, n):
    """Get the top N samples by grade."""
    # TODO: Sort descending and return first N
    pass

def filter_by_rock_types(samples, rock_types):
    """Filter samples matching any of the given rock types."""
    # TODO: Return samples where rock_type is in rock_types list
    pass

# Main code
if __name__ == "__main__":
    # Create sample data
    samples = [
        # TODO: Create samples with grades in range {grade_range}
    ]

    # TODO: Test each function
```

## Code Quality (Included in each task)

- Include docstrings for all functions
- Use meaningful variable names
- Add comments explaining complex logic
- Handle edge cases (empty lists, missing keys)

## Testing Your Code

Run the automated tests locally:

```bash
pytest tests/visible/ -v
```

Push to GitHub to see your score on the Actions tab.

## Tips

1. **List Comprehensions**: Prefer `[x for x in items if condition]` over explicit loops for creating filtered/transformed lists.

2. **Dictionary Access**: Use `dict.get(key, default)` to safely access values that might not exist.

3. **Sorting**: Use `sorted(list, key=lambda x: x['field'])` to sort list of dictionaries by a specific field.

4. **Copying Lists**: Use `list.copy()` or `list[:]` to create a copy before modifying.
