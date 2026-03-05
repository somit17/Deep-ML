# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Create the dataset from your notebook
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Weather': ['sunny', 'sunny', 'cloudy', 'rain', 'rain', 'rain',
                'cloudy', 'sunny', 'sunny', 'rain', 'sunny', 'cloudy',
                'cloudy', 'rain'],
    'Temperature': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool',
                    'cool', 'mild', 'cool', 'mild', 'mild', 'mild',
                    'hot', 'mild'],
    'Humidity': ['high', 'high', 'high', 'high', 'normal', 'normal',
                 'normal', 'high', 'normal', 'normal', 'normal', 'high',
                 'normal', 'high'],
    'Wind': ['weak', 'strong', 'weak', 'weak', 'weak', 'strong',
             'strong', 'weak', 'weak', 'weak', 'strong', 'strong',
             'weak', 'strong'],
    'Play': ['no', 'no', 'yes', 'yes', 'yes', 'no',
             'yes', 'no', 'yes', 'yes', 'yes', 'yes',
             'yes', 'no']
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)
print(f"\nTotal: Yes={len(df[df['Play']=='yes'])}, No={len(df[df['Play']=='no'])}")
print("="*70)

# Encode categorical variables
le_weather = LabelEncoder()
le_temp = LabelEncoder()
le_humidity = LabelEncoder()
le_wind = LabelEncoder()
le_play = LabelEncoder()

# Create encoded columns in the dataframe
df['Weather_enc'] = le_weather.fit_transform(df['Weather'])
df['Temp_enc'] = le_temp.fit_transform(df['Temperature'])
df['Humidity_enc'] = le_humidity.fit_transform(df['Humidity'])
df['Wind_enc'] = le_wind.fit_transform(df['Wind'])
df['Play_enc'] = le_play.fit_transform(df['Play'])

# Show the encoded dataset
print("\nEncoded Dataset (first few rows):")
print(df[['Weather', 'Weather_enc', 'Temperature', 'Temp_enc',
          'Humidity', 'Humidity_enc', 'Wind', 'Wind_enc', 'Play', 'Play_enc']].head())
print("="*70)

# Features and Target
X = df[['Weather_enc', 'Temp_enc', 'Humidity_enc', 'Wind_enc']]
y = df['Play_enc']

# Train Decision Tree
model = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)
model.fit(X, y)

# Visualize the tree
plt.figure(figsize=(12, 8))
plot_tree(model,
          feature_names=['Weather', 'Temperature', 'Humidity', 'Wind'],
          class_names=['No', 'Yes'],
          filled=True,
          rounded=True,
          fontsize=10)
plt.title("Decision Tree - Play Tennis Prediction", fontsize=14, fontweight='bold')
plt.show()

# Display tree as text
print("\nDecision Tree Rules:")
print("="*70)
tree_rules = export_text(model,
                         feature_names=['Weather', 'Temperature', 'Humidity', 'Wind'])
print(tree_rules)

# Feature Importance
print("\nFeature Importance:")
print("="*70)
importance_df = pd.DataFrame({
    'Feature': ['Weather', 'Temperature', 'Humidity', 'Wind'],
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)
print(importance_df)

