import numpy as np
import pandas as pd

# ============================================
# READING CSV FILES
# ============================================

print("="*50)
print("BASIC CSV READING")
print("="*50)

# Basic read
dataframe = pd.read_csv('DataStore/customers-1000.csv')
print("Basic read (first 5 rows):")
print(dataframe.head())
print("\n")

# Read with specific separator (if not comma)
df_tab = pd.read_csv('DataStore/customers-1000.csv', sep=',')  # ',' is default
print("Read with explicit separator:")
print(df_tab.head())
print("\n")

# Read without header (if file has no column names)
df_no_header = pd.read_csv('DataStore/customers-1000.csv', header=None)
print("Read without header (first 5 rows):")
print(df_no_header.head())
print("\n")

# Read with custom column names
df_custom_names = pd.read_csv('DataStore/customers-1000.csv',
                              names=['ID', 'Customer_Name', 'Email', 'Phone',
                                     'Address', 'City', 'Country', 'Date_Joined'])
print("Read with custom column names:")
print(df_custom_names.head())
print("\n")

# ============================================
# USING INDEX_COL PARAMETER
# ============================================

print("="*50)
print("INDEX_COL EXAMPLES")
print("="*50)

# Use first column as index
df_index_col0 = pd.read_csv('DataStore/customers-1000.csv', index_col=0)
print("Using first column as index (index_col=0):")
print(df_index_col0.head())
print("Index values:", df_index_col0.index[:5].tolist())
print("\n")

# Use a specific column by name as index
df_index_customer = pd.read_csv('DataStore/customers-1000.csv',
                                index_col='Customer Id')
print("Using 'Customer Id' column as index:")
print(df_index_customer.head())
print("Index values:", df_index_customer.index[:5].tolist())
print("\n")

# Use multiple columns as index (MultiIndex)
df_multi_index = pd.read_csv('DataStore/customers-1000.csv',
                             index_col=['Country', 'City'])
print("Using 'Country' and 'City' as MultiIndex:")
print(df_multi_index.head())
print("MultiIndex example:", df_multi_index.index[:2].tolist())
print("\n")

# ============================================
# READING TEXT FILES
# ============================================

print("="*50)
print("TEXT FILE READING")
print("="*50)

# Using read_table (similar to read_csv but with \t as default separator)
df_table = pd.read_table('DataStore/customers-1000.csv', sep=',')
print("Using read_table with comma separator:")
print(df_table.head())
print("\n")

# Reading a space-separated text file (example - create a sample first)
# First, let's create a sample space-separated file
space_data = """Name Age City
John 25 NewYork
Anna 30 Paris
Peter 35 Berlin"""

with open('DataStore/sample_space.txt', 'w') as f:
    f.write(space_data)

# Read space-separated file
df_space = pd.read_csv('DataStore/sample_space.txt', sep='\s+')
print("Reading space-separated text file:")
print(df_space)
print("\n")

# Read with custom delimiter (e.g., pipe-separated)
pipe_data = """Name|Age|City
John|25|NewYork
Anna|30|Paris
Peter|35|Berlin"""

with open('DataStore/sample_pipe.txt', 'w') as f:
    f.write(pipe_data)

df_pipe = pd.read_csv('DataStore/sample_pipe.txt', sep='|')
print("Reading pipe-separated text file:")
print(df_pipe)
print("\n")

# ============================================
# ADVANCED READING OPTIONS
# ============================================

print("="*50)
print("ADVANCED READING OPTIONS")
print("="*50)

# Skip rows
df_skip = pd.read_csv('DataStore/customers-1000.csv', skiprows=5)
print("Skip first 5 rows:")
print(df_skip.head())
print("\n")

# Read only specific rows (nrows)
df_nrows = pd.read_csv('DataStore/customers-1000.csv', nrows=10)
print("Read only first 10 rows:")
print(df_nrows)
print("\n")

# Use specific columns (usecols)
df_usecols = pd.read_csv('DataStore/customers-1000.csv',
                         usecols=['Customer Id', 'First Name', 'Last Name', 'Email'])
print("Read only specific columns:")
print(df_usecols.head())
print("\n")

# Handle missing values
df_na = pd.read_csv('DataStore/customers-1000.csv',
                    na_values=['NA', 'N/A', 'null', ''])
print("Read with custom NA values:")
print(df_na.isna().sum())
print("\n")

# ============================================
# WRITING TO CSV FILES
# ============================================

print("="*50)
print("WRITING TO CSV")
print("="*50)

# Read the original data
df = pd.read_csv('DataStore/customers-1000.csv')

# Basic write to CSV
df.to_csv('DataStore/customers_copy.csv', index=False)
print("Basic CSV write completed (no index)\n")

# Write with index
df.to_csv('DataStore/customers_with_index.csv', index=True)
print("CSV write with index completed\n")

# Write specific columns
df[['Customer Id', 'First Name', 'Last Name', 'Email']].to_csv(
    'DataStore/customers_selected.csv', index=False)
print("Write selected columns completed\n")

# Write with different separator
df.to_csv('DataStore/customers_pipe.csv', sep='|', index=False)
print("Write with pipe separator completed\n")

# Write without header
df.to_csv('DataStore/customers_no_header.csv', header=False, index=False)
print("Write without header completed\n")

# Write with custom date format (if you have date columns)
# df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
# df.to_csv('DataStore/customers_dates.csv', index=False)

# ============================================
# WORKING WITH TEXT FILES - NOTES
# ============================================

print("="*50)
print("TEXT FILE NOTES")
print("="*50)

notes = """
TEXT FILE READING TIPS:
------------------------
1. Use pd.read_csv() for most text files (CSV, TSV, etc.)
2. Use sep parameter to specify delimiter:
   - sep=',' for comma-separated (default)
   - sep='\\t' for tab-separated
   - sep='\\s+' for whitespace-separated
   - sep='|' for pipe-separated

3. Common parameters:
   - header: which row to use as column names (None if no header)
   - names: custom column names
   - index_col: which column(s) to use as index
   - skiprows: rows to skip at beginning
   - nrows: number of rows to read
   - usecols: columns to read
   - na_values: values to treat as NA

4. Writing tips:
   - index=False to avoid writing row numbers
   - header=False to avoid writing column names
   - sep='\\t' for tab-separated output
"""

print(notes)

# ============================================
# PRACTICAL EXAMPLE - DATA PROCESSING
# ============================================

print("="*50)
print("PRACTICAL EXAMPLE - DATA PROCESSING")
print("="*50)

# Read data with specific index
df_processed = pd.read_csv('DataStore/customers-1000.csv',
                           index_col='Customer Id')

# Perform some operations
print("Data shape:", df_processed.shape)
print("\nColumn names:", df_processed.columns.tolist())
print("\nData types:")
print(df_processed.dtypes)

# Add a new column
df_processed['Full_Name'] = df_processed['First Name'] + ' ' + df_processed['Last Name']

# Save processed data
df_processed.to_csv('DataStore/customers_processed.csv')

print("\nProcessed data saved to 'DataStore/customers_processed.csv'")
print("New column 'Full_Name' added")

# Verify the processed file
df_verified = pd.read_csv('DataStore/customers_processed.csv')
print("\nFirst 3 rows of processed data:")
print(df_verified.head(3))