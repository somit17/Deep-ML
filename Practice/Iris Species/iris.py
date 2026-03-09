import pandas as pd
import numpy as np

csv_path = "../Iris Species/data-set/Iris.csv"
df = pd.read_csv(csv_path)
print(f"DATA-FRAME = {df.head(10)}")


#Check missing values
print(f"Missing Value Counts : {df.isnull().sum()}")


import seaborn as sns
import matplotlib.pyplot as plt

# Since the 'Id' column is just a sequence number, it won't be useful for analysis.
# We are creating a new variable by dropping it to exclude it from the plots.
df_visual = df.drop('Id', axis=1)

# Plotting the distribution and relationships of all features grouped by species
sns.pairplot(df_visual, hue="Species", palette="husl", markers=["o", "s", "D"])

# Display the plot
plt.show()