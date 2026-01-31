# GGY3601 Lab 3: Data Structures - Lists & Dictionaries

**Weight:** 10% of final grade
**Estimated Time:** 2-3 hours

## Purpose

This lab introduces Python's core data structures: lists and dictionaries. You will learn to organize, store, and manipulate collections of geological sample data efficiently.

## Learning Outcomes

By completing this lab, you will be able to:
- LO3.1: Create and manipulate lists of geological data
- LO3.2: Use dictionary structures for sample records
- LO3.3: Iterate over collections effectively
- LO3.4: Apply list comprehensions for data transformation

## Your Personalized Assignment

**See `ASSIGNMENT.md` for your unique parameters and test values.**

The ASSIGNMENT.md file contains your student-specific values that you must use in your solutions. These values are unique to you and are used for automated testing.

## Repository Structure

```
.
├── src/
│   ├── lab3_lists.py          # Task 1: List operations
│   ├── lab3_dictionaries.py   # Task 2: Dictionary operations
│   ├── lab3_sample_manager.py # Task 3: Managing sample collections
│   ├── lab3_statistics.py     # Task 4: Computing statistics
│   └── lab3_filters.py        # Task 5: Filtering and sorting
├── tests/
│   └── visible/               # Automated tests (visible to you)
├── ASSIGNMENT.md              # Your unique assignment parameters
└── README.md                  # This file
```

## Concepts Covered

### Lists
- Creating lists with `[]` or `list()`
- Indexing (positive and negative)
- Slicing (`list[start:end:step]`)
- List methods: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`
- List comprehensions: `[expression for item in iterable if condition]`

### Dictionaries
- Creating dictionaries with `{}` or `dict()`
- Accessing values with keys
- Dictionary methods: `keys()`, `values()`, `items()`, `get()`, `update()`
- Nested dictionaries
- Dictionary comprehensions

### Iteration
- `for` loops over lists and dictionaries
- `enumerate()` for index-value pairs
- `zip()` for parallel iteration

## Getting Started

1. Clone this repository to your local machine
2. Read `ASSIGNMENT.md` for your unique values
3. Complete each task in the `src/` directory
4. Run tests locally: `pytest tests/visible/ -v`
5. Push your code to see automated test results

## Submission

Push your completed code to this repository before the deadline. Your score is calculated from the automated tests.

## Academic Integrity

- **ALLOWED:** Lecture notes, official Python documentation, asking tutors
- **NOT ALLOWED:** Copying code, AI tools, sharing solutions

All submissions are checked with plagiarism detection software.
