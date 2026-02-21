# Pandas Toolkit

A collection of reusable pandas functions for common data operations.

## Installation

Clone the repository:
```bash
git clone <your-repo-url>
cd pandas_toolkit
```

Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install pandas
```

## Usage
```python
from pandas_toolkit import find_duplicates, rank_and_sort, get_nth_highest

See **Functions** section below for available methods.
```

## Functions

### Rankings (`rankings.py`)
- `get_nth_highest()` - Find nth highest unique value in a column
- `rank_and_sort()` - Rank values and sort by column

### Joins (`joins.py`)
- `left_join_and_select()` - Left join with column selection

### Patterns (`patterns.py`)
- `find_duplicates()` - Find duplicate values in a column
- `find_consecutive_values()` - Find values appearing N times consecutively

## License

MIT