# Matrix transpose operation explained:
# 
# *other_matrix.data        # Unpacks rows as separate arguments
# zip(*rows)                 # Pairs up elements by position (transposes)
# list(...)                  # Converts tuples to list

# Example with a concrete matrix:
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Step 1: Unpack the rows
rows = matrix  # rows = [[1, 2, 3], [4, 5, 6]]
# *rows unpacks to: [1, 2, 3], [4, 5, 6]

# Step 2: Zip the unpacked rows
# zip([1, 2, 3], [4, 5, 6]) creates: (1, 4), (2, 5), (3, 6)

# Step 3: Convert each tuple to a list
# list(...) converts to: [[1, 4], [2, 5], [3, 6]]

# Complete transpose operation:
transposed = [list(row) for row in zip(*matrix)]
# Result: [[1, 4], [2, 5], [3, 6]]