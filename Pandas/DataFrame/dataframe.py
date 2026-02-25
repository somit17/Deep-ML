import pandas as pd
import numpy as np

# Set random seed for reproducible results
# Ensures same random numbers are generated each time
np.random.seed(123)

# Define lists of states and years to use in our dataset
states = ['California', 'Texas', 'Florida', 'New York', 'Illinois',
          'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
years = [2019, 2020, 2021, 2022, 2023]

# Generate random data using numpy random functions
# np.random.choice() randomly selects 15 items from the given list
# np.random.randint() generates 15 random integers between min and max
data = {
    'State': np.random.choice(states, 15),
    'Year': np.random.choice(years, 15),
    'Pop': np.random.randint(5000000, 40000000, 15)
}

# Create initial DataFrame from the dictionary
# pd.DataFrame() converts dictionary to DataFrame with default integer index
dataframe = pd.DataFrame(data)
print(f"DataFrame - \n{dataframe}")

# Create DataFrame with custom column specification
# columns parameter specifies which columns to include (can't add new columns this way)
# index parameter sets custom index starting from 1 to 15
dataframe_add_col = pd.DataFrame(data,
                                 columns=['State','Year','Pop','Debt'],
                                 index=range(1, 16)  # Dynamic index based on data length
                                 )
# Add Debt column by direct assignment
# Creates new column with 15 random integer values
dataframe_add_col['Debt'] = np.random.randint(0, 10000000, 15)
print(f"DataFrame after adding column -\n{dataframe_add_col}")

# Add another new column called 'Random'
# Direct assignment with bracket notation adds new column to DataFrame
dataframe_add_col['Random'] = np.random.randint(0, 10, 15)
print(f"DataFrame after adding column -\n{dataframe_add_col}")

# Delete the 'Random' column using del keyword
# del permanently removes the specified column from DataFrame
del dataframe_add_col['Random']
print(f"DataFrame after adding column -\n{dataframe_add_col}")

# Access and modify specific cell using .loc[]
# .loc[] is label-based indexing - first parameter is row label, second is column label
# This line attempts to set value at row 1, column 2 to 2032 (Note: column 2 is 'Pop')
dataframe_add_col.loc[1,2]=2032  # This might cause issues as column labels are strings
print(f"Value at (2,1) = {dataframe_add_col.loc[[1,2]]}")

# Rename column labels
# rename() method changes column names using dictionary mapping
# inplace=True modifies the original DataFrame instead of returning a new one
dataframe_add_col.rename(columns={'State':'STATES','Year':'YEAR'},inplace=True)
print(f"DataFrame - \n{dataframe_add_col}")