import pandas as pd
import numpy as np

# ============================================
# SERIES CREATION AND OPERATIONS
# ============================================

# Create first Series with custom index labels
series_a = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
# Output: a    7.3, c   -2.5, d    3.4, e    1.5

# Create second Series with different index labels
series_b = pd.Series([-2.1, 3.6, -1.5, 4, 3.1],
               index=['a', 'c', 'e', 'f', 'g'])
# Output: a   -2.1, c    3.6, e   -1.5, f    4.0, g    3.1

print(series_a)
print(series_b)

# Demonstrate automatic data alignment - pandas aligns by index labels
# Only indices present in both Series are added, others become NaN
print(series_a + series_b)
# Output: a    5.2, c    1.1, d    NaN, e    0.0, f    NaN, g    NaN

# ============================================
# DATAFRAME CREATION AND OPERATIONS
# ============================================

# Create first DataFrame with 3x3 matrix (values 0-8)
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                   index=['Ohio', 'Texas', 'Colorado'])
# Output:
#           b    c    d
# Ohio    0.0  1.0  2.0
# Texas   3.0  4.0  5.0
# Colorado 6.0  7.0  8.0

# Create second DataFrame with 4x3 matrix (values 0-11)
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# Output:
#         b    d    e
# Utah   0.0  1.0  2.0
# Ohio   3.0  4.0  5.0
# Texas  6.0  7.0  8.0
# Oregon 9.0 10.0 11.0

print(df1)
print(df2)

# DataFrame subtraction with automatic alignment on both index and columns
# Result contains union of indices and columns, missing values become NaN
print(df1 - df2)
# Output shows alignment by both row indices and column labels

# ============================================
# DATAFRAMES WITH DIFFERENT COLUMNS
# ============================================

# Create DataFrames with completely different column structures
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
print(df1)
print(df2)

# Subtraction results in DataFrame with both columns, values NaN where no match
print(df1 - df2)
# Output:
#      A   B
# 0  NaN NaN
# 1  NaN NaN

# ============================================
# ARITHMETIC METHODS WITH FILL VALUES
# ============================================

# Create DataFrames with different shapes for fill_value demonstration
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)), columns=list('abcd'))
# Output: 3x4 matrix (0-11) with columns a,b,c,d

df2 = pd.DataFrame(np.arange(20).reshape((4, 5)), columns=list('abcde'))
# Output: 4x5 matrix (0-19) with columns a,b,c,d,e

print(df1)
print(df2)

# Modify a specific value to demonstrate non-uniform data
df2.loc[1, 'b'] = 150
print(df2)

# Add DataFrames with fill_value=0 (replaces NaN with 0 before operation)
print(df1.add(df2, fill_value=0))
# This allows operation even where indices/columns don't match

# Demonstrate reciprocal operations
print(1/df1)  # Element-wise reciprocal
print(df1.rdiv(1))  # Same as 1/df1 (rdiv = reverse division)

# Reindex df1 to match df2's columns, filling missing with 0
df1.reindex(columns=df2.columns, fill_value=0)

# ============================================
# OPERATIONS BETWEEN DATAFRAME AND SERIES
# ============================================

# NumPy array broadcasting demonstration
arr = np.arange(12).reshape((3, 4))
print(arr)
print(arr[0])  # First row
print(arr - arr[0])  # Broadcast subtract first row from all rows

# DataFrame and Series operations (broadcasting)
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]  # First row as Series
print(frame)
print(series)

# Subtract Series from DataFrame - broadcasts Series across rows
print(f"Series - Frame {series - frame}")

# Series with different index alignment during operations
series = pd.Series(range(3), index=['b', 'e', 'f'])
print(series)
result = series + frame  # Aligns by column names
print(f"Result - {result}")

# ============================================
# FUNCTION APPLICATION AND MAPPING
# ============================================

# Create random DataFrame for function demonstrations
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)

# Apply NumPy universal functions (element-wise)
print(np.abs(frame))

# Define lambda function to find range (max-min)
f = lambda x: x.max() - x.min()
print(frame.apply(f))  # Apply to columns (axis=0 by default)
print(frame.apply(f, axis='columns'))  # Apply to rows

# Function returning Series for more detailed statistics
def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])

print(frame.apply(f))

# Formatting functions
format = lambda x: '%.2f' % x
print(format)

# Apply formatting to entire DataFrame (element-wise)
print(frame.map(format))  # Note: map() replaces deprecated applymap()

# Apply formatting to single column
print(frame['e'].map(format))

# ============================================
# SORTING AND RANKING
# ============================================

# Series sorting by index
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_index())  # Sort by index labels

# DataFrame sorting
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])
print(frame.sort_index())  # Sort rows by index
print(frame.sort_index(axis=1))  # Sort columns by column names
print(frame.sort_index(axis=1, ascending=False))  # Descending order

# Series sorting by values
obj = pd.Series([4, 7, -3, 2])
print(obj.sort_values())  # Sort by values

# Handling NaN in sorting
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.sort_values())  # NaN placed at end by default

# DataFrame sorting by specific columns
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame)
print(frame.sort_values(by='b'))  # Sort by column 'b'
print(frame.sort_values(by=['a', 'b']))  # Sort by multiple columns

# Ranking demonstrations
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())  # Average rank for ties (default)
print(obj.rank(method='first'))  # Assign ranks in order of appearance
print(obj.rank(ascending=False, method='max'))  # Max rank for ties, descending

# Column-wise ranking
frame = pd.DataFrame({'b': [4.3, 7, -3, 2],
                      'a': [0, 1, 0, 1],
                      'c': [-2, 5, 8, -2.5]})
print(frame.rank(axis='columns'))  # Rank across columns for each row

# ============================================
# AXIS INDEXES WITH DUPLICATE LABELS
# ============================================

# Series with duplicate index labels
obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj.index.is_unique)  # Check if index has unique values
print(obj['a'])  # Returns Series with both 'a' values
print(obj['c'])  # Returns single value (unique index)

# DataFrame with duplicate index labels
df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print(df.loc['b'])  # Returns all rows with index 'b'