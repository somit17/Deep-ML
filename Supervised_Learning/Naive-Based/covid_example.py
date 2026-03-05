import pandas as pd
from sklearn.naive_bayes import BernoulliNB

# Simple data
data = {
    'Covid': ['Y','N','Y','N','Y','N','Y','Y','N','N'],
    'Flu': ['N','Y','Y','N','N','N','N','N','Y','Y'],
    'Fever': ['Y','Y','Y','N','Y','Y','Y','N','Y','N']
}

df = pd.DataFrame(data)

# Convert to numbers - FIX: Add astype(int)
X = df[['Covid', 'Flu']].replace({'Y': 1, 'N': 0}).astype(int)
y = df['Fever'].replace({'Y': 1, 'N': 0}).astype(int)

# Train
model = BernoulliNB()
model.fit(X, y)

# Test
test = pd.DataFrame({'Covid': [1, 0, 1, 0], 'Flu': [1, 0, 0, 1]})
preds = model.predict(test)

print("Predictions:")
for i, (c, f) in enumerate(zip(test['Covid'], test['Flu'])):
    print(f"Covid={'Y' if c else 'N'}, Flu={'Y' if f else 'N'} → Fever={'YES' if preds[i] else 'NO'}")