import pandas as pd
import numpy as np

"""
PANDAS DATA MANIPULATION - COMPREHENSIVE GUIDE
===============================================
This file demonstrates key pandas operations for data cleaning and transformation
"""

# ============================================================================
# 1. MISSING DATA HANDLING
# ============================================================================

print("="*70)
print("1. MISSING DATA HANDLING")
print("="*70)

# Working with missing values (NaN) in pandas
string_data = pd.Series(['A', 'B', np.nan, 'CS'])
print("Original Series with NaN:")
print(string_data)
print("\nisnull() - Detects missing values:")
print(string_data.isnull())  # Returns boolean mask (True for missing)

# None is also treated as NaN in pandas
string_data[0] = None
print("\nAfter setting first element to None:")
print(string_data.isnull())  # None converts to NaN

from numpy import nan as NA

# Different ways to handle missing values in Series
data = pd.Series([1, NA, 3.5, NA, 7])
print("\nSeries with missing values:")
print(data)
print("\ndropna() - Removes missing values:")
print(data.dropna())  # Drops all rows with NaN
print("\nnotnull() - Boolean mask for non-missing:")
print(data[data.notnull()])  # Alternative way to filter out NaN

# Working with missing data in DataFrames
data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
print("\nDataFrame with missing values:")
print(data)

# dropna() on DataFrame - removes any row with at least one NaN
cleaned = data.dropna()
print("\ndropna() - Removes rows with ANY missing values:")
print(cleaned)

# how='all' - only remove rows where ALL values are missing
print("\ndropna(how='all') - Removes rows where ALL values are missing:")
print(data.dropna(how='all'))

# Working with columns instead of rows
data[1] = NA  # Set entire column to missing
print("\nAfter setting column 1 to all NA:")
print(data)
print("\ndropna(axis=1, how='all') - Remove columns where ALL values are missing:")
print(data.dropna(axis=1, how='all'))  # axis=1 for columns

# thresh parameter - minimum number of non-NA values
df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA  # First 4 rows, column 1 set to NA
df.iloc[:2, 2] = NA  # First 2 rows, column 2 set to NA
print("\nDataFrame with strategic missing values:")
print(df)
print("\ndropna() - Default (drops any row with NA):")
print(df.dropna())
print("\ndropna(thresh=2) - Keep rows with at least 2 non-NA values:")
print(df.dropna(thresh=2))

# ============================================================================
# 2. FILLING MISSING DATA
# ============================================================================

print("\n" + "="*70)
print("2. FILLING MISSING DATA")
print("="*70)

# fillna() - Replace missing values with specified values
print("\nfillna(0) - Replace all NA with 0:")
print(df.fillna(0))

# Fill different columns with different values
print("\nfillna({1: 0.5, 2: 0}) - Column-specific fill values:")
print(df.fillna({1: 0.5, 2: 0}))

# inplace=True - Modify original DataFrame
df.fillna(0, inplace=True)
print("\nAfter fillna(0, inplace=True):")
print(df)

# Forward fill (ffill) - Propagate last valid observation forward
df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA  # Rows 2-5, column 1 set to NA
df.iloc[4:, 2] = NA  # Rows 4-5, column 2 set to NA
print("\nNew DataFrame for ffill demonstration:")
print(df)
print("\nffill() - Forward fill (propagates last valid value):")
print(df.ffill())  # Replaces NaN with previous row's value
print("\nffill(limit=2) - Forward fill with limit of 2 consecutive fills:")
print(df.ffill(limit=2))

# Fill with statistical measures
data = pd.Series([1., NA, 3.5, NA, 7])
print("\nSeries for statistical filling:")
print(data)
print("\nfillna(data.median()) - Fill with median value:")
print(data.fillna(data.median()))  # Useful for imputation

# ============================================================================
# 3. REMOVING DUPLICATES
# ============================================================================

print("\n" + "="*70)
print("3. REMOVING DUPLICATES")
print("="*70)

# Create DataFrame with duplicate rows
data = pd.DataFrame({
    'k1': ['one', 'two'] * 3 + ['two'],
    'k2': [1, 1, 2, 3, 3, 4, 4]
})
print("Original DataFrame (has duplicates):")
print(data)

# Identify duplicates
print("\nduplicated() - Boolean mask for duplicate rows:")
print(data.duplicated())  # True for rows that are duplicates of previous rows

# Remove duplicates
print("\ndrop_duplicates() - Remove duplicate rows (keeps first occurrence):")
print(data.drop_duplicates())

# Add another column
data['v1'] = range(7)
print("\nDataFrame with new column 'v1':")
print(data)

# Remove duplicates based on specific columns
print("\ndrop_duplicates(['k1']) - Remove duplicates based only on 'k1' column:")
print(data.drop_duplicates(['k1']))

# keep='last' - Keep last occurrence instead of first
print("\ndrop_duplicates(['k1', 'k2'], keep='last') - Keep last occurrence:")
print(data.drop_duplicates(['k1', 'k2'], keep='last'))

# ============================================================================
# 4. MAPPING AND TRANSFORMING VALUES
# ============================================================================

print("\n" + "="*70)
print("4. MAPPING AND TRANSFORMING VALUES")
print("="*70)

# Create food dataset
data = pd.DataFrame({
    'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef',
             'Bacon', 'pastrami', 'honey ham', 'nova lox'],
    'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]
})
print("Original food data:")
print(data)

# Dictionary for mapping food to animal source
meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}

# str.lower() - Convert all strings to lowercase for consistent mapping
lowercased = data['food'].str.lower()
print("\nLowercased food values:")
print(lowercased)

# map() - Apply mapping dictionary to Series
data['animal'] = lowercased.map(meat_to_animal)
print("\nAfter mapping food to animal source:")
print(data)

# Alternative: map with lambda function
print("\nAlternative mapping with lambda:")
print(data['food'].map(lambda x: meat_to_animal[x.lower()]))

# ============================================================================
# 5. REPLACING VALUES
# ============================================================================

print("\n" + "="*70)
print("5. REPLACING VALUES")
print("="*70)

# replace() - Replace values in Series/DataFrame
data = pd.Series([1., -999., 2., -999., -1000., 3.])
print("Original Series with placeholder values:")
print(data)

# Replace single value
print("\nreplace(-999, np.nan) - Replace -999 with NaN:")
print(data.replace(-999, np.nan))

# Replace multiple values with same replacement
print("\nreplace([-999, -1000], np.nan) - Replace multiple values:")
print(data.replace([-999, -1000], np.nan))

# Replace multiple values with different replacements
print("\nreplace([-999, -1000], [np.nan, 0]) - Different replacements:")
print(data.replace([-999, -1000], [np.nan, 0]))

# Replace using dictionary
print("\nreplace({-999: np.nan, -1000: 0}) - Dictionary mapping:")
print(data.replace({-999: np.nan, -1000: 0}))

# ============================================================================
# 6. RENAMING INDEXES AND COLUMNS
# ============================================================================

print("\n" + "="*70)
print("6. RENAMING INDEXES AND COLUMNS")
print("="*70)

# Create DataFrame with custom index
data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print("Original DataFrame:")
print(data)

# Map function to transform index
transform = lambda x: x[:4].upper()  # First 4 characters, uppercase
data.index = data.index.map(transform)
print("\nAfter index.map() - Transformed index:")
print(data)

# rename() - Create new object with renamed axes
print("\nrename(index=str.title, columns=str.upper) - Function mapping:")
print(data.rename(index=str.title, columns=str.upper))

# rename() with dictionary mapping
print("\nrename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'}):")
print(data.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'}))

# inplace=True - Modify original
data.rename(index={'OHIO': 'INDIANA'}, inplace=True)
print("\nAfter rename with inplace=True:")
print(data)

# ============================================================================
# 7. BINNING (DISCRETIZATION)
# ============================================================================

print("\n" + "="*70)
print("7. BINNING (DISCRETIZATION)")
print("="*70)

# cut() - Bin continuous values into discrete intervals
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]  # Define bin edges
cats = pd.cut(ages, bins)
print("Age data binned into categories:")
print(cats)
print("\nCategory codes (bin assignments):")
print(cats.codes)  # Numerical codes for each bin
print("\nCategory labels:")
print(cats.categories)  # Unique categories

# right=False - Change interval inclusivity
print("\npd.cut(ages, [18,26,36,61,100], right=False) - Left-inclusive bins:")
print(pd.cut(ages, [18, 26, 36, 61, 100], right=False))

# Custom labels
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print("\ncut() with custom labels:")
print(pd.cut(ages, bins, labels=group_names))

# cut() on random data
data = np.random.rand(20)
print("\ncut(data, 4) - Equal-width binning (4 bins):")
print(pd.cut(data, 4, precision=2))

# qcut() - Quantile-based binning (equal number of points per bin)
data = np.random.randn(1000)
cats = pd.qcut(data, 4)  # 4 quantiles (quartiles)
print("\nqcut(data, 4) - Quantile-based binning:")
print(cats)
print("\nCustom quantiles [0, 0.1, 0.5, 0.9, 1]:")
print(pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.]))

# ============================================================================
# 8. DUMMY VARIABLES (ONE-HOT ENCODING)
# ============================================================================

print("\n" + "="*70)
print("8. DUMMY VARIABLES (ONE-HOT ENCODING)")
print("="*70)

# Create categorical DataFrame
df = pd.DataFrame({
    'key': ['b', 'b', 'a', 'c', 'a', 'b'],
    'data1': range(6)
})
print("Original DataFrame:")
print(df)

# get_dummies() - Convert categorical variable into dummy/indicator variables
print("\nget_dummies(df['key']) - One-hot encoding:")
print(pd.get_dummies(df['key']))

# Join dummies with original data
dummies = pd.get_dummies(df['key'], prefix='key')  # prefix adds column prefix
df_with_dummy = df[['data1']].join(dummies)
print("\nOriginal data joined with dummy variables:")
print(df_with_dummy)

# Combine binning with dummy variables
np.random.seed(12345)
values = np.random.rand(10)
print("\nRandom values for binning:")
print(values)

bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
binned = pd.cut(values, bins)
print("\nBinned values:")
print(binned)
print("\nDummy variables from bins:")
print(pd.get_dummies(binned))