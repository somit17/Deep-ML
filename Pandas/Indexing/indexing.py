import pandas as pd
import numpy as np

# ====================================================================
# PART 1: SERIES INDEX OPERATIONS
# ====================================================================

print("="*60)
print("PART 1: SERIES INDEX OPERATIONS")
print("="*60)

# Create a Series with custom index labels
# range(3) generates values [0,1,2] and we assign index ['a','b','c']
series = pd.Series(range(3), index=['a', 'b', 'c'])
index = series.index  # Extract the Index object

print(f"Original Series:\n{series}")
print(f"Index object: {index}")
print(f"Type of index: {type(index)}")
print()

# Index slicing examples
print("Index Slicing Examples:")
print(f"index[:1] (first element): {index[:1]}")      # Select from start to position 1
print(f"index[:-1] (all except last): {index[:-1]}")  # Select all except last
print(f"index[1:] (from position 1): {index[1:]}")    # Select from position 1 to end
print(f"index[-1:] (last element): {index[-1:]}")     # Select only last element
print()

# ====================================================================
# PART 2: CREATING AND USING INDEX OBJECTS
# ====================================================================

print("="*60)
print("PART 2: CREATING AND USING INDEX OBJECTS")
print("="*60)

# Create an Index object from numpy array
# pd.Index creates a reusable pandas Index object
labels = pd.Index(np.arange(3))
print(f"Created Index object: {labels}")
print(f"Type: {type(labels)}")
print()

# Create Series using the Index object
# Demonstrates reusing an Index for multiple Series
series_2 = pd.Series([1.5, -2.5, 0], index=labels)
print(f"Series created with Index object:\n{series_2}")
print()

# Check if Series index is the same object as labels
# 'is' checks for object identity (same memory location)
print(f"series_2.index is labels? {series_2.index is labels}")  # True
print()

# ====================================================================
# PART 3: DATAFRAME CREATION AND INDEX CHECKING
# ====================================================================

print("="*60)
print("PART 3: DATAFRAME CREATION AND INDEX CHECKING")

# Create a DataFrame with state data
data = {
    'State': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Year': [2000, 2001, 2002, 2003, 2004, 2005],
    'Pop': [1.5, 1.6, 2.5, 4.2, 3.5, 1.9]
}
dataframe = pd.DataFrame(data)
print("Original DataFrame:")
print(dataframe)
print()

# Check membership in DataFrame
# 'in' operator checks if value exists in columns/index
print(f"'State' in dataframe.columns? {'State' in dataframe.columns}")  # True
print(f"2003 in dataframe.index? {2003 in dataframe.index}")  # False (index is 0-5)
print()

# Create Index with duplicate labels
# pandas allows duplicate index labels (use with caution)
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
print(f"Index with duplicate labels: {dup_labels}")
print()

# DataFrame slicing examples
print("DataFrame slicing examples:")
print(f"dataframe[0::] (all rows):\n{dataframe[0::]}")
print(f"dataframe[::] (all rows):\n{dataframe[::]}")
print(f"dataframe[0::-1] (reverse from start):\n{dataframe[0::-1]}")
print(f"dataframe[0::1] (forward all rows):\n{dataframe[0::1]}")
print()

# Select specific column using .loc[]
print("Select 'State' column using .loc[]:")
print(dataframe.loc[:, ['State']])
print()

# ====================================================================
# PART 4: ESSENTIAL FUNCTIONALITY - REINDEXING
# ====================================================================

print("="*60)
print("PART 4: REINDEXING OPERATIONS")
print("="*60)

# Create a Series with custom index
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print("Original Series:")
print(obj)
print()

# Reindex to new index order
# reindex() rearranges data to match new index, fills missing with NaN
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print("After reindexing to ['a','b','c','d','e']:")
print(obj2)  # 'e' will have NaN value
print()

# Create Series with gaps in index
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print("Series with gaps in index:")
print(obj3)
print()

# Reindex with forward fill method
# method='ffill' fills missing values with last valid observation
print("After reindexing range(6) with forward fill:")
print(obj3.reindex(range(6), method='ffill'))
print()

# Create DataFrame with missing index
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                     index=['a', 'c', 'd'],
                     columns=['Ohio', 'Texas', 'California'])
print("DataFrame with missing index 'b':")
print(frame)
print()

# Reindex rows to include missing index 'b'
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print("After reindexing rows to include 'b':")
print(frame2)
print()

# Reindex columns to new order
states = ['Texas', 'Utah', 'California']
frame3 = frame.reindex(columns=states)
print("After reindexing columns to ['Texas','Utah','California']:")
print(frame3)
print()

# ====================================================================
# PART 5: DROPPING ENTRIES
# ====================================================================

print("="*60)
print("PART 5: DROPPING ENTRIES")
print("="*60)

# Create Series for drop examples
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print("Original Series:")
print(obj)
print()

# Drop single element by index label
new_obj = obj.drop('c')
print("After dropping 'c':")
print(new_obj)
print()

# Drop multiple elements by passing list
print("After dropping ['d', 'c']:")
print(obj.drop(['d', 'c']))
print()

# Create DataFrame for drop examples
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print("Original DataFrame:")
print(data)
print()

# Drop rows by index labels (axis=0 is default)
print("After dropping rows 'Colorado' and 'Ohio':")
print(data.drop(['Colorado', 'Ohio']))
print()

# Drop columns using axis parameter
print("After dropping column 'two' (axis=1):")
print(data.drop('two', axis=1))
print()

print("After dropping columns ['two', 'four']:")
print(data.drop(['two', 'four'], axis='columns'))
print()

# ====================================================================
# PART 6: INDEXING, SELECTION, AND FILTERING (FIXED)
# ====================================================================

print("="*60)
print("PART 6: INDEXING, SELECTION, AND FILTERING")
print("="*60)

# Series indexing examples
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print("Original Series:")
print(obj)
print()

# 1. Label-based indexing (using index labels)
print("1. Label-based indexing:")
print(f"obj['b'] = {obj['b']}")  # Single label
print(f"obj[['b', 'a', 'd']] = \n{obj[['b', 'a', 'd']]}")  # List of labels
print(f"obj['b':'c'] = \n{obj['b':'c']}")  # Label slice (includes both ends)
print()

# 2. Position-based indexing (using iloc)
print("2. Position-based indexing with iloc:")
print(f"obj.iloc[1] = {obj.iloc[1]}")  # Single position
print(f"obj.iloc[[1, 3]] = \n{obj.iloc[[1, 3]]}")  # List of positions
print(f"obj.iloc[2:4] = \n{obj.iloc[2:4]}")  # Position slice (excludes end)
print()

# 3. Boolean indexing
print("3. Boolean indexing:")
print(f"obj[obj < 2] = \n{obj[obj < 2]}")  # Values less than 2
print()

# 4. Mixed approach (works but ambiguous)
print("4. Mixed approach (works but not recommended):")
print(f"obj[2:4] = \n{obj[2:4]}")  # This works but is ambiguous
print("Note: Better to be explicit with obj.iloc[2:4]")
print()

# ====================================================================
# PART 7: DATAFRAME INDEXING OPERATIONS
# ====================================================================

print("="*60)
print("PART 7: DATAFRAME INDEXING OPERATIONS")
print("="*60)

# Create DataFrame for indexing examples
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print("Original DataFrame:")
print(data)
print()

# Column selection
print("Select single column 'two':")
print(data['two'])  # Returns Series
print()

print("Select multiple columns ['three', 'one']:")
print(data[['three', 'one']])  # Returns DataFrame
print()

# Row selection and boolean indexing
print("Rows where 'three' column > 5:")
print(data[data['three'] > 5])
print()

# Boolean DataFrame operations
print("Boolean mask (data < 5):")
print(data < 5)
print()

print("Set all values < 5 to 0:")
data[data < 5] = 0
print(data)
print()

# ====================================================================
# PART 8: SELECTION WITH LOC AND ILOC
# ====================================================================

print("="*60)
print("PART 8: SELECTION WITH LOC AND ILOC")
print("="*60)

# Reset data for clean examples
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print("Reset DataFrame:")
print(data)
print()

# loc examples (label-based)
print("LOC EXAMPLES:")
print(f"data.loc['Colorado', ['two', 'three']]:\n{data.loc['Colorado', ['two', 'three']]}")
print()
print(f"data.loc[:'Utah', 'two']:\n{data.loc[:'Utah', 'two']}")
print()

# iloc examples (position-based)
print("ILOC EXAMPLES:")
print(f"data.iloc[2, [3, 0, 1]]:\n{data.iloc[2, [3, 0, 1]]}")
print()
print(f"data.iloc[2]:\n{data.iloc[2]}")
print()
print(f"data.iloc[[1, 2], [3, 0, 1]]:\n{data.iloc[[1, 2], [3, 0, 1]]}")
print()

# Combined boolean and positional indexing
print("Combined boolean and positional indexing:")
print(f"data.iloc[:, :3][data.three > 5]:\n{data.iloc[:, :3][data.three > 5]}")
print()

# ====================================================================
# PART 9: PRACTICAL EXAMPLES AND SUMMARY
# ====================================================================

print("="*60)
print("PART 9: PRACTICAL EXAMPLES")
print("="* 60)

# Create a practical dataset
sales_data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [100, 250, 175, 300, 225],
    'Region': ['North', 'South', 'East', 'West', 'North']
}
df_sales = pd.DataFrame(sales_data, index=['P1', 'P2', 'P3', 'P4', 'P5'])
print("Sales DataFrame:")
print(df_sales)
print()

# Practical operations
print("1. Select Product and Sales columns:")
print(df_sales[['Product', 'Sales']])
print()

print("2. Select rows where Sales > 200:")
print(df_sales[df_sales['Sales'] > 200])
print()

print("3. Select specific row by label using loc:")
print(df_sales.loc['P3'])
print()

print("4. Select specific row by position using iloc:")
print(df_sales.iloc[2])
print()

print("5. Select subset using loc with conditions:")
print(df_sales.loc[df_sales['Region'] == 'North', ['Product', 'Sales']])
print()

print("="*60)
print("END OF ALL OPERATIONS")
print("="*60)