import numpy as np
import pandas as pd

# Creating a basic Series from a list
# pd.Series() converts a list to a pandas Series object with default integer index
series = pd.Series([3,2,4,-5])

print(series)
print(type(series))

# Accessing Series properties
# .index returns the index labels of the Series (default 0,1,2,...)
print(f"Index - {series.index}")
# .values returns the numpy array of the Series data
print(f"Values - {series.values}")

# Creating Series with custom index labels
# index parameter allows specifying custom labels instead of default integers
series_manual_index = pd.Series([1,2,3,4], index=['a','b','c','d'])
print(f"Index - {series_manual_index.index}")
print(f"Values - {series_manual_index.values}")

# Updating Series values using index labels
# Direct assignment using index label updates a single element
series_manual_index['b'] = 6
# .loc[] accesses a group of rows by label(s) for assignment
series_manual_index.loc[['a','c','d']] = 100
print(f"After updating values - {series_manual_index}")

# Applying numpy mathematical functions to Series
# np.exp() calculates exponential of each element (e^x) and returns a new Series
print(f"{np.exp(series_manual_index)}")

# Checking index membership
# 'in' operator checks if a specific index label exists in the Series
print(f"Check if index exists : - {'e' in series_manual_index}")

# Creating Series from dictionary
# Dictionary keys become index labels, values become Series data
sdata = {'HR': 3500 , 'Marketing':7100 , 'Indoor':1600 , 'Outdoor':500}
series_sdata = pd.Series(sdata)
print(f"After making series -\n{series_sdata}")

# Reindexing a Series with new index labels
# When reindexing, existing values are matched by label, missing labels get NaN
states = ['South','East','North','West']
series_states = pd.Series(series_sdata, index=states)
print(f"Series -\n{series_states}")

# Checking for missing values
# pd.isnull() returns boolean Series indicating which values are null (NaN)
print(pd.isnull(series_states))
# pd.notnull() returns boolean Series indicating which values are not null
print(pd.notnull(series_states))

# Series arithmetic with alignment
# When adding Series, pandas automatically aligns data by index labels
# Missing values in either Series result in NaN in the output
print(series_sdata + series_states)